# Generated by Django 4.1.7 on 2023-03-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='num_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]
