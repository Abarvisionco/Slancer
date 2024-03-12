# Generated by Django 5.0.1 on 2024-01-28 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_resume_create_time_alter_resume_update_date'),
        ('users', '0004_remove_user_resume_remove_user_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='district',
            name='city',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='school',
            name='district',
        ),
        migrations.RemoveField(
            model_name='examworks',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='nationalcode',
            name='field',
        ),
        migrations.RemoveField(
            model_name='school',
            name='national_code',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='school',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='resume',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='ExamWorks',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='NationalCode',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
