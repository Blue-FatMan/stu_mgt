from django.shortcuts import render
from django.views.generic import ListView
from acheve_mgt.models import Student, MyClass, ScoreShip, Course
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required
def person(request, pk):
    user = request.user
    myclass = MyClass.objects.all()[0]
    student = myclass.student.get(pk=pk)
    scoreship = ScoreShip.objects.get(student=student, course=student.course.all()[0])
    term = scoreship.get_term_display()
    return render(request, 'acheve_mgt/person.html', context={
        'user': user,
        'myclass': myclass,
        'student': student,
        'term': term,
    })

@login_required
def person_data(request, pk):
    myclass = MyClass.objects.all()[0]
    students = myclass.student.all()

    data = []
    s = students.get(pk=pk)
    count = s.course.count()
    id = 1
    for c in s.course.all():
        d = {}
        d['id'] = id
        id = id + 1
        d['course_name'] = c.name
        score = ScoreShip.objects.get(student=s, course=c)
        d['exam_score'] = score.exam_score
        d['daily_score'] = score.daily_score
        d['sum_score'] = score.exam_score*0.7 + score.daily_score*0.3
        data.append(d)

    result = {
        "code": 0,
        "msg":"",
        "count": count,
        "data": data,
    }
    return JsonResponse(result)

@login_required
def single_course(request, pk):
    user = request.user
    myclass = MyClass.objects.all()[0]
    student = myclass.student.all()[0]

    course = student.course.get(pk=pk)
    scoreship = ScoreShip.objects.get(student=student, course=course)
    term = scoreship.get_term_display()

    students_of_course = course.score.all()
    student_score_data = []
    count = 1
    for s in students_of_course:
        d = {}
        d['order'] = count
        count += 1
        d['name'] = s.name
        d['number'] = s.number

        scoreship_tmp = ScoreShip.objects.get(student=s, course=course)
        d['exam_score'] = scoreship_tmp.exam_score
        d['daily_score'] = scoreship_tmp.daily_score
        d['sum_score'] = scoreship_tmp.exam_score*0.7 + scoreship_tmp.daily_score*0.3
        d['id'] = s.id
        student_score_data.append(d)

    return render(request, 'acheve_mgt/single_course.html', context={
        'user': user,
        'myclass': myclass,
        'course': course,
        'student_score_data': student_score_data,
        'term': term,
    })

@login_required
def view_course(request):
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
    return render(request, 'acheve_mgt/view_course.html', context={
        'user': user,
        'myclass': myclass,
        'student': student,
        'course_list': course_list,
        'term': term,
    })

@login_required
def score_together(request):
    user = request.user
    myclass = MyClass.objects.all()[0]
    students = myclass.student.all()
    courses = students[0].course.all()

    scoreship = ScoreShip.objects.get(student=students[0], course=courses[0])
    term = scoreship.get_term_display()



    score_together_data = []
    count = 1
    for s in students:
        d = {}
        d['order'] = count
        count += 1
        d['number'] = s.number
        d['name'] = s.name

        four_course_score = 0
        courses_score = []
        courses_name = []
        for c in courses:
            tmp = ScoreShip.objects.get(student=s, course=c)
            each_course_score = tmp.exam_score*0.7 + tmp.daily_score*0.3
            four_course_score += each_course_score
            courses_score.append(each_course_score)
            courses_name.append(c.name)

        d['courses_score'] = courses_score
        d['courses_name'] = courses_name
        d['avg_score'] = four_course_score/4
        d['id'] = s.id
        score_together_data.append(d)


    return render(request, 'acheve_mgt/score_together.html', context={
        'user': user,
        'myclass': myclass,
        'score_together_data': score_together_data,
        'row_score_together': score_together_data[0],
        'term': term,
    })

@login_required
def score_rating(request):
    user = request.user
    myclass = MyClass.objects.all()[0]
    students = myclass.student.all()
    courses = students[0].course.all()

    scoreship = ScoreShip.objects.get(student=students[0], course=courses[0])
    term = scoreship.get_term_display()

    rating_data = []
    order = 1
    for c in courses:
        d = {}
        d['order'] = order
        order += 1
        d['course_name'] = c.name
        ra, rb, rc, rd, re = 0, 0, 0, 0, 0

        for s in students:
            scoreship = ScoreShip.objects.get(student=s, course=c)
            score = scoreship.daily_score*0.3 + scoreship.exam_score*0.7
            if score >=90 and score <= 100:
                ra += 1
            elif score>=80 and score <90:
                rb += 1
            elif score>=70 and score<80:
                rc += 1
            elif score>=60 and score<70:
                rd += 1
            else:
                re += 1
        d['a'] = ra
        d['b'] = rb
        d['c'] = rc
        d['d'] = rd
        d['e'] = re
        rating_data.append(d)

    all_course_rating = {}
    ra, rb, rc, rd, re = 0, 0, 0, 0, 0
    for s in students:
        sum_score = 0
        for c in courses:
            scoreship = ScoreShip.objects.get(student=s, course=c)
            score = scoreship.daily_score * 0.3 + scoreship.exam_score * 0.7
            sum_score += score

            if score < 60:
                re += 1
                break
        else:
            avg_score = sum_score/s.course.count()
            if avg_score >=90 and avg_score <= 100:
                ra += 1
            elif avg_score>=80 and avg_score <90:
                rb += 1
            elif avg_score>=70 and avg_score<80:
                rc += 1
            elif avg_score>=60 and avg_score<70:
                rd += 1
            else:
                re += 1
    all_course_rating['a'] = ra
    all_course_rating['b'] = rb
    all_course_rating['c'] = rc
    all_course_rating['d'] = rd
    all_course_rating['e'] = re
    all_course_rating['order'] = order
    all_course_rating['four_courses'] = '四门课程总评'


    return render(request, 'acheve_mgt/score_rating.html', context={
        'user': user,
        'myclass': myclass,
        'rating_data': rating_data,
        'all_course_rating': all_course_rating,
        'term': term,
    })
