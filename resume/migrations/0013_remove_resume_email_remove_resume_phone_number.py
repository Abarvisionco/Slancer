# Generated by Django 5.0.1 on 2024-02-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_alter_resume_resume_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='email',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='phone_number',
        ),
    ]
