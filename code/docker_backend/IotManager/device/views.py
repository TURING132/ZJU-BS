from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from user.models import CustomUser
from .models import Device
import json


@csrf_exempt
@require_GET
def get_message(request):
    user_id = request.GET.get('user_id')
    device_id = request.GET.get('device_id')

    try:
        # 检查用户是否存在
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '当前用户不存在'})
        try:
            device = Device.objects.get(user=user, device_id=device_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '当前设备不存在'})

        message_list = device.messages.all().values('type', 'text', 'timestamp').order_by('-timestamp')

        return JsonResponse({'status': 'success', 'message_list': list(message_list)})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@csrf_exempt
@require_GET
def get(request):
    # 从URL参数中获取user_id
    user_id = request.GET.get('user_id')
    try:
        # 检查用户是否存在
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '当前用户不存在'})

        # 获取用户的所有设备
        devices = Device.objects.filter(user=user)

        # 构造设备列表
        device_list = [
            {
                'id': device.device_id,
                'name': device.device_name,
                'location': device.device_location,
                'type': device.device_type,
                'status': device.device_status,
                'is_online': device.is_online
            }
            for device in devices
        ]

        return JsonResponse({'status': 'success', 'devices': device_list})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
@require_POST
def add(request):
    try:
        # 从请求中获取JSON数据
        data = json.loads(request.body)

        # 获取JSON数据中的参数
        user_id = data.get('user_id')
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '用户不存在'})

        device_id = data.get('device_id')
        device_name = data.get('device_name')
        device_location = data.get('device_location')
        device_type = data.get('device_type')
        device_status = 'off'

        # 检查device_id是否重复
        if Device.objects.filter(user=user, device_id=device_id).exists():
            return JsonResponse({'status': 'error', 'message': '设备已经存在，不可重复创建'})

        # 创建新的Device对象并保存
        new_device = Device.objects.create(
            user=user,
            device_id=device_id,
            device_name=device_name,
            device_location=device_location,
            device_type=device_type,
            device_status=device_status
        )

        return JsonResponse({'status': 'success', 'message': '设备添加成功'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': '错误的JSON格式'})


@csrf_exempt
@require_POST
def modify(request):
    try:
        # 从请求中获取JSON数据
        data = json.loads(request.body)

        # 获取JSON数据中的参数
        user_id = data.get('user_id')
        device_id = data.get('device_id')
        device_name = data.get('device_name')
        device_location = data.get('device_location')
        device_type = data.get('device_type')
        device_status = data.get('device_status')
        is_online = data.get('is_online')
        # 获取设备对象
        try:
            device = Device.objects.get(device_id=device_id, user_id=user_id)
        except Device.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '设备不存在'})

        # 修改设备信息
        if device_name:
            device.device_name = device_name
        if device_location:
            device.device_location = device_location
        if device_type:
            device.device_type = device_type
        if device_status:
            device.device_status = device_status
        if is_online:
            device.is_online = is_online

        # 保存修改后的设备信息
        device.save()

        return JsonResponse({'status': 'success', 'message': '设备信息成功修改'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': '无效的JSON格式'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


