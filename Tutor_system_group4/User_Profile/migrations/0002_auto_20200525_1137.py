# Generated by Django 3.0.4 on 2020-05-25 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='briefintroduction',
            field=models.CharField(blank=True, default='暂无', help_text='个人简介，所在学校/学习情况等', max_length=100, null=True,
                                   verbose_name='教师信息'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='briefintroduction',
            field=models.CharField(blank=True, default='暂无', help_text='个人简介，所在学院/专业/履历等', max_length=100, null=True,
                                   verbose_name='教师信息'),
        ),
    ]