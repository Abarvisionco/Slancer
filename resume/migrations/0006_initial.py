# Generated by Django 5.0.1 on 2024-01-28 12:03

import django.db.models.deletion
import django_quill.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0005_remove_city_state_remove_district_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام شهر')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهر ها',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='نام رشته')),
            ],
            options={
                'verbose_name': 'رشته',
                'verbose_name_plural': 'رشته ها',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام استان')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان ها',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ناحیه')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.city', verbose_name='شهر')),
            ],
            options={
                'verbose_name': 'ناحیه',
                'verbose_name_plural': 'نواحی',
            },
        ),
        migrations.CreateModel(
            name='NationalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.IntegerField(unique=True, verbose_name='کد ملی')),
                ('fullname', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('gender', models.CharField(choices=[('male', 'پسر'), ('femal', 'دختر')], default='male', max_length=20, verbose_name='جنسیت')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.field', verbose_name='رشته')),
            ],
            options={
                'verbose_name': 'کد ملی',
                'verbose_name_plural': 'کد های ملی',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', django_quill.fields.QuillField()),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('linkedin', models.URLField(blank=True, max_length=500, null=True, verbose_name='آدرس لینکدین')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس محل سکونت')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('phone_number', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='شماره تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('resume_file', models.FileField(upload_to='resume_files/%Y/%m/', verbose_name='فایل رزومه شخصی')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'رزومه',
                'verbose_name_plural': 'رزومه ها',
            },
        ),
        migrations.CreateModel(
            name='ExamWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان نمونه کار')),
                ('link', models.URLField(blank=True, null=True, verbose_name='آدرس نمونه کار')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume', verbose_name='رزومه')),
            ],
            options={
                'verbose_name': 'نمونه کار',
                'verbose_name_plural': 'نمونه کار ها',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دوره آموزشی')),
                ('description', models.TextField(verbose_name='توشیحات دوره')),
                ('level', models.CharField(choices=[('a', 'مقدماتی'), ('b', 'متوسط'), ('c', 'پیشرفته')], default='a', max_length=5, verbose_name='سطح دوره')),
                ('start_date', models.DateField(verbose_name='تاریخ شروع دوره')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاریخ اتمام دوره')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume', verbose_name='رزومه')),
            ],
            options={
                'verbose_name': 'دوره آموزشی',
                'verbose_name_plural': 'دوره های آموزشی',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام هنرستان')),
                ('about', django_quill.fields.QuillField(blank=True, null=True, verbose_name='درباره هنرستان')),
                ('email', models.EmailField(blank=True, max_length=500, null=True, verbose_name='ایمیل')),
                ('link', models.URLField(blank=True, max_length=1000, null=True, verbose_name='آدرس اینترنتی وبسایت')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت فعالیت')),
                ('activity_date', models.IntegerField(blank=True, null=True, verbose_name='سال شروع فعالیت')),
                ('phone_number', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='شماره تفن')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.district', verbose_name='ناحیه در شهر')),
                ('national_code', models.ManyToManyField(to='resume.nationalcode', verbose_name='کد ملی')),
            ],
            options={
                'verbose_name': 'هنرستان',
                'verbose_name_plural': 'هنرستان ها',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.school', verbose_name='هنرستان'),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('a', 'مقدماتی'), ('b', 'متوسط'), ('c', 'پیشرفته')], default='a', max_length=5, verbose_name='سطح مهارت')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume', verbose_name='رزومه')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'مهارت ها',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.state', verbose_name='استان'),
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='عنوان شغل')),
                ('co_name', models.CharField(max_length=200, verbose_name='نام سازمان محل فعالیت')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('start_date', models.DateField(verbose_name='تاریخ شروع')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume', verbose_name='رزومه')),
            ],
            options={
                'verbose_name': 'سابقه شغلی',
                'verbose_name_plural': 'سوابق شغلی',
            },
        ),
    ]
