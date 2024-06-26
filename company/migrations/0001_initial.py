# Generated by Django 5.0.3 on 2024-05-08 11:23

import django.db.models.deletion
import django_quill.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0026_examworks_update_date'),
        ('users', '0005_remove_user_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=200, verbose_name='نام شرکت یا سازمان')),
                ('image', models.ImageField(upload_to='companies/%Y/%m', verbose_name='عکس')),
                ('company_url', models.URLField(blank=True, max_length=1000, null=True, verbose_name='آدرس اینترنتی')),
                ('about', django_quill.fields.QuillField(verbose_name='درباره شرکت')),
                ('description', django_quill.fields.QuillField(verbose_name='توضیحات، مزایا و نحوه دوره کارآموزی برای کارآموزان')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.district', verbose_name='ناحیه قرار گیری شرکت')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.field', verbose_name='حوضه کاری بر اساس رشته های هنرستان')),
                ('send_resume', models.ManyToManyField(blank=True, null=True, to='resume.resume', verbose_name='رزومه های ارسال شده')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.state', verbose_name='استان محل قرار گیری شرکت')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user', models.Model),
        ),
    ]
