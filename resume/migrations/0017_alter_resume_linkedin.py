# Generated by Django 5.0.3 on 2024-03-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_alter_resume_birth_day_alter_resume_birth_mount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس لینکدین'),
        ),
    ]
