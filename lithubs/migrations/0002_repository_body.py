# Generated by Django 4.1.7 on 2023-03-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
