# Generated by Django 5.0.3 on 2024-05-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0026_examworks_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth_day',
            field=models.IntegerField(blank=True, null=True, verbose_name='روز تولد'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='birth_mount',
            field=models.IntegerField(blank=True, null=True, verbose_name='ماه تولد'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='سال تولد'),
        ),
    ]
