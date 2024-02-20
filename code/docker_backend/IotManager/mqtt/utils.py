import json
import time

import paho.mqtt.client as mqtt
from django.apps import apps

from IotManager import settings
from device.models import Device
from message.models import Message


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('$SYS/brokers/+/metrics/bytes/received')
        mqtt_client.subscribe('$SYS/brokers/+/metrics/bytes/sent')
        mqtt_client.subscribe('$SYS/brokers/+/clients/+/connected')
        mqtt_client.subscribe('$SYS/brokers/+/clients/+/disconnected')
        mqtt_client.subscribe('iot/#')  # 订阅主题
    else:
        print('Bad connection. Code:', rc)


def receive_message(mqtt_client, topic, device_id, payload):
    try:
        data = json.loads(payload)
        device_id = data.get('device_id')
        message_type = data.get('type')
        if not device_id or not message_type:
            mqtt_client.publish('response/' + topic, '请提供设备id和类型')

        valid_types = dict(Message.MESSAGE_TYPES).keys()
        if message_type not in valid_types:
            mqtt_client.publish('response/' + topic, "无效的消息类型")
            return

        if message_type == 'location':
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            if not latitude or not longitude:
                mqtt_client.publish('response/' + topic, '请提供经纬度内容')
                return
            text = json.dumps({
                'latitude': latitude,
                'longitude': longitude
            })
        else:
            text = data.get('text')
        if not text:
            mqtt_client.publish('response/' + topic, '请提供消息内容')

        device = Device.objects.get(device_id=device_id)
        message = Message.objects.create(device=device, type=message_type, text=text)

        mqtt_client.publish('response/' + topic, f'消息成功接收')
    except json.JSONDecodeError as e:
        mqtt_client.publish('response/' + topic, f'JSON 格式错误 {e}')
    except Device.DoesNotExist:
        mqtt_client.publish('response/' + topic, f'设备 {device_id} 不存在')
    except Exception as ex:
        mqtt_client.publish('response/' + topic, f'捕获到异常: {ex}')


def on_message(mqtt_client, userdata, msg):
    # print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    if msg.topic.startswith('iot/'):
        try:
            device_id = msg.topic.split('/')[1]
            receive_message(mqtt_client, msg.topic, device_id, msg.payload)
        except IndexError:
            mqtt_client.publish('response/' + msg.topic, f'Error: 未提供设备id - {msg.topic}')
    elif msg.topic.endswith('/bytes/received'):
        mqtt_app_config = apps.get_app_config('mqtt')
        mqtt_app_config.received_bytes = int(msg.payload.decode('utf-8'))
        # print('received', mqtt_app_config.received_bytes)
    elif msg.topic.endswith('/bytes/sent'):
        mqtt_app_config = apps.get_app_config('mqtt')
        mqtt_app_config.sent_bytes = int(msg.payload.decode('utf-8'))
        # print('sent', mqtt_app_config.sent_bytes)
    elif msg.topic.endswith('disconnected'):
        data = json.loads(msg.payload.decode('utf-8'))
        client_id = data.get('clientid')
        print('client disconnected:', client_id)
        device = Device.objects.get(device_id=client_id)
        device.is_online = False
        device.save()
    elif msg.topic.endswith('connected'):
        data = json.loads(msg.payload.decode('utf-8'))
        client_id = data.get('clientid')
        print('client connected:', client_id)
        device = Device.objects.get(device_id=client_id)
        device.is_online = True
        device.save()


def connect_to_mqtt():
    retries = 0
    while retries < 5000000:
        try:
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
            client.connect(
                host=settings.MQTT_SERVER,
                port=settings.MQTT_PORT,
                keepalive=settings.MQTT_KEEPALIVE
            )
            return client
        except:
            time.sleep(5)
            retries += 1
    return None
