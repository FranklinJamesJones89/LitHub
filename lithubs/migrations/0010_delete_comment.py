# Generated by Django 4.1.7 on 2023-03-29 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0009_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]