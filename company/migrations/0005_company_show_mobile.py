# Generated by Django 5.0.3 on 2024-05-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='show_mobile',
            field=models.BooleanField(default=True, verbose_name='نمایش شماره تلفن همراه به کارآموزان'),
        ),
    ]
