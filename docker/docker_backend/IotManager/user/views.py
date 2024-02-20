from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import check_password
from .models import CustomUser
import json


@csrf_exempt
@require_POST
def register(request):
    # 获取前端发送的注册请求数据
    data = json.loads(request.body.decode('utf-8'))

    # 从请求数据中提取用户名、密码等信息
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # 检查用户名是否重复
    if CustomUser.objects.filter(username=username).exists():
        response_data = {'status': 'error', 'message': '用户名重复'}
        return JsonResponse(response_data)

    # 检查邮箱是否重复
    if CustomUser.objects.filter(email=email).exists():
        response_data = {'status': 'error', 'message': '邮箱已注册账号'}
        return JsonResponse(response_data)

    user = CustomUser.objects.create(username=username, email=email, password=make_password(password))

    response_data = {'status': 'success', 'message': '账号注册成功'}
    return JsonResponse(response_data)


@csrf_exempt
@require_POST
def check(request):
    # 获取前端发送的请求数据
    data = json.loads(request.body.decode('utf-8'))

    # 从请求数据中提取用户名和密码信息
    email = data.get('email')
    password = data.get('password')

    try:
        # 使用Django的authenticate函数检查用户名和密码是否匹配
        user = CustomUser.objects.get(email=email)

        if check_password(password, user.password):
            # 密码正确
            response_data = {'status': 'success', 'username': user.username, 'user_id': user.user_id,
                             'email': user.email}
        else:
            # 密码不正确
            response_data = {'status': 'error', 'message': '密码错误'}
    except CustomUser.DoesNotExist:
        # 用户不存在
        response_data = {'status': 'error', 'message': '邮箱未注册账号'}

    return JsonResponse(response_data)
