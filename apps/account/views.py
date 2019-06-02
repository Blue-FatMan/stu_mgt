from django.shortcuts import render
from django.contrib import auth
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required

from .models import User

import re


# Create your views here.
@require_POST
def login(request):
    """
    登入函数
    """
    data = request.POST
    user = auth.authenticate(username=data['username'], password=data['password'])

    message = ''
    if user:
        if user.USER_TYPE == 'regular':
            message = '用户不具有登入权限！'
        elif user.USER_TYPE == 'admin':
            auth.login(request, user)
    else:
        message = '信息错误！'
    return render(request, 'account/login.html', context={
        'message': message,
    })

@require_GET
def test(request):
    return render(request, 'account/test.html')







# @require_POST
# def register(request):
#     """注册函数"""
#     data = request.data
#     username = data.get('username')
#     password = data.get('password')
#
#     message = ''
#     if username and password:
#         if User.objects.filter(username=username).exists():
#             message = '用户名已存在！'
#         else:
#             if not re.match('[0-9a-zA-Z]{8,16}', password):
#                 User.objects.create(username=username, password=password)
#                 return render(request, 'account/')
#             else:
#                 message = '密码格式不对，请输入8至16位字母、数字组成的密码！'
#     else:
#         message = '注册信息未填写！'



