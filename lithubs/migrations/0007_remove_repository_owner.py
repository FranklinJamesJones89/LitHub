# Generated by Django 4.1.7 on 2023-03-03 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0006_repository_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='owner',
        ),
    ]