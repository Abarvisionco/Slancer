# Generated by Django 5.0.3 on 2024-03-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_resume_link_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='examworks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exam_works/%Y/%m', verbose_name='عکس نمونه کار'),
        ),
    ]
