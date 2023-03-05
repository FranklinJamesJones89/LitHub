# Generated by Django 4.1.7 on 2023-03-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0004_alter_repository_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='form',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repository',
            name='synopsis',
            field=models.TextField(max_length=1000),
        ),
    ]
