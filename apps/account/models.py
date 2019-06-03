from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class UserManager(models.Manager):
#     use_in_migrations = True
#
#     def get_by_natural_key(self, username):
#         return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class User(AbstractUser):
    USER_TYPE = (
        ('admin', '管理员'),
        ('regular', '普通用户'),
        ('anon', '匿名用户'),
    )
    username = models.CharField(max_length=20, unique=True, verbose_name='用户姓名')
    is_superuser = models.BooleanField(default=0, verbose_name='是否是超级用户')
    user_type = models.CharField(max_length=20, choices=USER_TYPE,
                                 default='regular', verbose_name='用户类型')
    create_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
