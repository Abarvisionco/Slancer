# Generated by Django 5.0.3 on 2024-05-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatroom_last_response_alter_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
