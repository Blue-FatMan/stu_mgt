from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required


from .models import User

import re


# Create your views here.

def login(request):
    """
    登入函数
    """
    message = ''
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            if user:
                if user.password == password:
                    if user.user_type == 'anon':
                        message = '用户不具有登入权限！'
                    else:
                        auth.login(request, user)
                        return redirect('/account/index/')
                else:
                    message = '密码错误！'
            else:
                message = '用户不存在！'
        else:
            message = '信息未填写！'

    return render(request, 'account/login.html', context={
        'message': message,
    })

@login_required
def index(request):
    return render(request, 'account/index.html')

@login_required
def logout(request):
    user = request.user
    auth.logout(request)
    return redirect('/account/login/')

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



