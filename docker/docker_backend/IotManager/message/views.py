from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from device.models import Device
from user.models import CustomUser
from .models import Message
import json


# Create your views here.
@csrf_exempt
@require_POST
def post(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        device_id = data.get('device_id')
        message_type = data.get('type')
        if message_type == 'location':
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            text = json.dumps({
                'latitude': latitude,
                'longitude': longitude
            })
        else:
            text = data.get('text')

        # Assuming 'device_id' is a unique identifier for your Device model
        device = Device.objects.get(device_id=device_id)

        valid_types = dict(Message.MESSAGE_TYPES).keys()
        if message_type not in valid_types:
            return JsonResponse({'status': 'error', 'message': '消息类型不符合要求'})

        # Create a new Message
        message = Message.objects.create(device=device, type=message_type, text=text)

        return JsonResponse({'status': 'success', 'message': f"接收到消息，message_id = {message.id}"})

    except Device.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '设备当前不存在'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@csrf_exempt
@require_GET
def location_list(request):
    user_id = request.GET.get('user_id')

    if not user_id:
        return JsonResponse({'status': 'error', 'message': '请提供用户id'})

    try:
        user = CustomUser.objects.get(user_id=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '当前用户不存在'})

    latest_location_messages = []
    for device in user.devices.all():
        latest_location_message = Message.objects.filter(device=device, type='location').order_by('-timestamp').first()
        if not latest_location_message:
            continue
        try:
            location_data = json.loads(latest_location_message.text)
            latitude = location_data.get('latitude')
            longitude = location_data.get('longitude')

            latest_location_messages.append({
                'name': device.device_name,
                'id':device.device_id,
                'timestamp': latest_location_message.timestamp,
                'latitude': latitude,
                'longitude': longitude
            })
        except json.JSONDecodeError:
            # 处理JSON解析错误
            return JsonResponse({'status': 'error', 'message': 'JSON解析错误'})

    return JsonResponse({'status': 'success', 'position_list': latest_location_messages})


@csrf_exempt
@require_GET
def location_history(request):
    user_id = request.GET.get('user_id')
    device_id = request.GET.get('device_id')
    if not user_id or not device_id:
        return JsonResponse({'status': 'error', 'message': '请提供user_id和device_id.'})

    try:
        user = CustomUser.objects.get(user_id=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '当前用户不存在'})

    try:
        device = Device.objects.get(user=user, device_id=device_id)
    except Device.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '当前设备不存在'})

    location_messages = Message.objects.filter(device=device, type='location').order_by('-timestamp')

    history_list = []
    for message in location_messages:
        try:
            location_data = json.loads(message.text)
            latitude = location_data.get('latitude')
            longitude = location_data.get('longitude')

            history_list.append({
                'timestamp': message.timestamp,
                'latitude': latitude,
                'longitude': longitude
            })
        except json.JSONDecodeError:
            # 处理JSON解析错误
            return JsonResponse({'status': 'error', 'message': 'JSON解析错误'})

    response_data = {'status': 'success', 'history_list': history_list}
    return JsonResponse(response_data)
