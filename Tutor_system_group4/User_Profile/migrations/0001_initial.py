# Generated by Django 3.0.4 on 2020-04-22 11:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
                ('age', models.PositiveIntegerField(default=15)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=2)),
                ('grade', models.CharField(
                    choices=[('0', '小学一年级至三年级'), ('1', '小学四年级至六年级'), ('2', '初一'), ('3', '初二'), ('4', '初三'), ('5', '高一'),
                             ('6', '高二'), ('7', '高三'), ('8', '其他')], default='5', max_length=2)),
                ('mailbox', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('age', models.PositiveIntegerField(default=20)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=2)),
                ('grade', models.CharField(
                    choices=[('0', '大一'), ('1', '大二'), ('2', '大三'), ('3', '大四'), ('4', '研一'), ('5', '研二'), ('6', '研三'),
                             ('7', '其他')], default='1', max_length=2)),
                ('mailbox', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('student_teached',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User_Profile.Student')),
                ('teacher_user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile',
                                      to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile',
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]
