# Generated by Django 4.2 on 2023-04-03 19:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0005_repository'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='pexels-victor-448835_nqesnt', max_length=255, null=True),
        ),
    ]