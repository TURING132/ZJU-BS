import json

from django.apps import apps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from device.models import Device


# Create your views here.

@csrf_exempt
@require_POST
def post(request):
    mqtt_app_config = apps.get_app_config('mqtt')
    client = mqtt_app_config.client
    try:
        data = json.loads(request.body.decode('utf-8'))
        device_id = data.get('device_id')
        message = data.get('message')

        client.publish('response/iot/' + device_id, message)

        return JsonResponse({'status': 'success', 'message': f"消息发送成功"})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@csrf_exempt
@require_GET
def bytes(request):
    mqtt_app_config = apps.get_app_config('mqtt')
    return  JsonResponse({'received_bytes':mqtt_app_config.received_bytes,
                          'sent_bytes':mqtt_app_config.sent_bytes})