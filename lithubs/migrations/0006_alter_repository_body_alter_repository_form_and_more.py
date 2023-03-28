# Generated by Django 4.1.7 on 2023-03-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0005_repository_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='form',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='repository',
            name='genre',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='repository',
            name='image',
            field=models.ImageField(blank=True, default='default-repo-image.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='repository',
            name='synopsis',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
