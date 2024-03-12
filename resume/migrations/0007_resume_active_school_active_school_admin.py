# Generated by Django 5.0.1 on 2024-01-28 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='active',
            field=models.BooleanField(default=True, verbose_name='وضعیت نمایش رزومه به دیگران'),
        ),
        migrations.AddField(
            model_name='school',
            name='active',
            field=models.CharField(choices=[('a', 'تایید شده'), ('b', 'در انتظار تایید'), ('c', 'تایید نشده'), ('d', 'اجازه فعالیت دارد اما تایید نشده')], default='b', max_length=2, verbose_name='وضعیت تاییدیه'),
        ),
        migrations.AddField(
            model_name='school',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='مدیریت'),
        ),
    ]
