from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from acheve_mgt.models import MyClass, Student, ScoreShip, Course
from django.http import HttpResponse, JsonResponse


from .models import User

import re


# Create your views here.
def login(request):
    """
    登入函数
    """
    message = ''
    if request.user.is_authenticated:
        return redirect('/account/index/')
    else:
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
def logout(request):
    user = request.user
    auth.logout(request)
    return redirect('/account/login/')

@login_required
def index(request):
    user = request.user
    myclass = MyClass.objects.all()[0]
    return render(request, 'account/index.html', context={
        'user': user,
        'myclass': myclass,
    })

@login_required
def student_message(request):
    """index视图的数据接口"""
    myclass = MyClass.objects.all()[0]
    students = myclass.student.all()
    count = students.count()

    data = []
    order = 1
    for s in students:
        core_data = {}  #很有必要，防止引用
        core_data['id'] = order
        order += 1
        core_data['number'] = s.number
        core_data['name'] = s.name
        data.append(core_data)
    result = {
        "code": 0,
        "msg":"",
        "count": count,
        "data": data,
    }
    return JsonResponse(result)

@login_required
def course(request):
    user = request.user
    myclass = MyClass.objects.all()[0]
    student = myclass.student.all()[0]
    courses = student.course.all()
    course_list = []
    count = 1
    for course in courses:
        d = {}
        d['order'] = count
        count += 1
        d['name'] = course.name
        d['teacher_name'] = course.teacher_name
        d['id'] = course.id
        course_list.append(d)

    scoreship = ScoreShip.objects.get(student=student, course=courses[0])
    term = scoreship.get_term_display()
    return render(request, 'account/course.html', context={
        'user': user,
        'myclass': myclass,
        'student': student,
        'course_list': course_list,
        'term': term,
    })











@require_GET
def test(request):
    return render(request, 'account/test.html')





