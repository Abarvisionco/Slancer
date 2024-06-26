# Generated by Django 5.0.3 on 2024-05-12 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='companies/%Y/%m', verbose_name='عکس'),
        ),
    ]
