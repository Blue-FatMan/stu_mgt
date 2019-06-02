# Generated by Django 2.0 on 2019-06-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190602_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', '管理员'), ('regular', '普通用户')], default='regular', max_length=20, verbose_name='用户类型'),
        ),
    ]
