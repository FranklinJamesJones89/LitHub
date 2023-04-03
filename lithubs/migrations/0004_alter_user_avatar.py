# Generated by Django 4.2 on 2023-04-03 17:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='v1680540852/xrl5mtwt3wzqyh992ovs.svg', max_length=255),
        ),
    ]