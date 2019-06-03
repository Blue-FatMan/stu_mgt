import xadmin
from xadmin import views

from acheve_mgt.models import MyClass, Student, Course, ScoreShip


class MyClassAdmin(object):
    list_display = ['name', 'grade', 'dept']
    ordering = ['-create_time', 'name', 'grade']
    serch_fields = ['name', 'grade', 'dept']


class StudentAdmin(object):
    list_display = ['number', 'name', 'myclass', 'student__course_name']
    ordering = ['-create_time', 'number']


class CourseAdmin(object):
    list_display = ['name', 'teacher_name', 'score']
    ordering = ['-create_time', 'score', 'name']


class ScoreShipAdmin(object):
    list_display = ['term', 'course', 'student', 'daily_score', 'exam_score']
    ordering = ['-create_time', 'term']


#后台中各个注册模型排列顺序与注册顺序有关
xadmin.site.register(MyClass, MyClassAdmin)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(ScoreShip, ScoreShipAdmin)