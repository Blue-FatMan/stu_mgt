# Generated by Django 2.0 on 2019-06-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acheve_mgt', '0017_remove_scoreship_sum_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclass',
            name='name',
            field=models.CharField(choices=[('w1', '物联网工程1班'), ('w2', '物联网工程2班'), ('j1', '计算机1班'), ('j2', '计算机2班'), ('t0', '通信工程卓越班'), ('t1', '通信工程1班'), ('t2', '通信工程2班')], max_length=20, verbose_name='班级名称'),
        ),
    ]