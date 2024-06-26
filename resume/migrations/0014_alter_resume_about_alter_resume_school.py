# Generated by Django 5.0.1 on 2024-03-01 19:38

import django.db.models.deletion
import django_quill.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_remove_resume_email_remove_resume_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='about',
            field=django_quill.fields.QuillField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.school', verbose_name='هنرستان'),
        ),
    ]
