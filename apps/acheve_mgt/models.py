from django.db import models


# Create your models here.


class MyClass(models.Model):
    """
    班级模型
    """
    DEPT = (
        ('信息', '信息工程学院'),
        # ('理', '理学院'),
        # ('软件', '软件学院'),
        # ('体育', '体育学院'),
        # ('艺术', '艺术学院'),
        # ('外国语', '外国语学院'),
    )
    GRADE = (
        ('18', '2018级'),
        ('17', '2017级'),
        ('16', '2016级'),
        ('15', '2015级'),
    )
    CLASS_NAME = (
        ('w1', '物联网工程1班'),
        ('w2', '物联网工程2班'),
        ('j1', '计算机1班'),
        ('j2', '计算机2班'),
        ('t0', '通信工程卓越班'),
        ('t1', '通信工程1班'),
        ('t2', '通信工程2班'),
    )
    # dept = models.CharField(max_length=20, default='信息',
    #                         choices=DEPT, verbose_name='学院')
    # grade = models.CharField(max_length=20, default='16', choices=GRADE, verbose_name='年级')
    # name = models.CharField(max_length=20, choices=CLASS_NAME, default='w1', verbose_name='班级名称')
    dept = models.CharField(max_length=20, choices=DEPT, verbose_name='学院')
    grade = models.CharField(max_length=20, choices=GRADE, verbose_name='年级')
    name = models.CharField(max_length=20, choices=CLASS_NAME, verbose_name='班级名称')
    create_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        db_table = 'myclass'
        verbose_name = '班级'
        verbose_name_plural = verbose_name
        unique_together = (('grade', 'name'), )

    def __str__(self):
        return self.get_name_display()


class Student(models.Model):
    """
    学生模型
    """
    myclass = models.ForeignKey(MyClass, on_delete=models.CASCADE,
                                related_name='student', verbose_name='班级')
    number = models.CharField(max_length=20, unique=True, verbose_name='学号')
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    create_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    课程模型
    """
    score = models.ManyToManyField(Student, related_name='course',
                                   through='ScoreShip', verbose_name='学生')
    name = models.CharField(max_length=20, verbose_name='课程名称')
    teacher_name = models.CharField(max_length=20, verbose_name='任课老师')
    create_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        unique_together = (('name', 'teacher_name'), )

    def __str__(self):
        return self.name


class ScoreShip(models.Model):
    """
    成绩模型, 同时关联课程和学生
    """
    TERM = (
        ('2016.1', '2016-2017年第一学期'),
        ('2016.2', '2016-2017年第二学期'),
        ('2017.1', '2017-2018年第一学期'),
        ('2017.2', '2017-2018年第二学期'),
        ('2018.1', '2018-2019年第一学期'),
        ('2018.2', '2018-2019年第二学期'),
        ('2019.1', '2019-2020年第一学期'),
        ('2019.2', '2019-2020年第二学期'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='scoreship', verbose_name='课程')
    student = models.ForeignKey(Student, on_delete=models.CASCADE,
                                related_name='scoreship', verbose_name='学生')

    term = models.CharField(max_length=20, choices=TERM, default='2018.2', verbose_name='学期')
    daily_score = models.FloatField(verbose_name='平时成绩')
    exam_score = models.FloatField(verbose_name='考试成绩')
    create_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        db_table = 'scoreship'
        verbose_name = '成绩'
        verbose_name_plural = verbose_name
        unique_together = (('course', 'student', 'term'), )

    def __str__(self):
        return "course: %s, student: %s, daily_score: %s, exam_score: %s" % \
               (self.course, self.student, self.daily_score, self.exam_score)

    def get_sum_score(self):
        """计算每个学生的单科成绩总评分"""
        sum_score = self.exam_score*0.7 + self.daily_score*0.3
        return sum_score
    get_sum_score.short_description = '单科成绩总评分'

    #abandent
    # sum_score = models.FloatField(default=0, verbose_name='单科成绩总评分')


