# Generated by Django 5.0.3 on 2024-03-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_alter_resume_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='school',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام هنرستان'),
        ),
    ]
