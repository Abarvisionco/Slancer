# Generated by Django 5.0.3 on 2024-05-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_company_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, help_text='میتواند خالی باشد.', null=True, verbose_name='آدرس'),
        ),
    ]
