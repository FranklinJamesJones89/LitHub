# Generated by Django 4.1.7 on 2023-03-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0013_alter_repository_num_of_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='num_of_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
