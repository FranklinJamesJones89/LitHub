# Generated by Django 4.1.7 on 2023-03-14 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0006_alter_room_host_alter_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
    ]
