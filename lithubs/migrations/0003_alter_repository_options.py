# Generated by Django 4.1.7 on 2023-03-09 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0002_repository_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'ordering': ['-updated', '-created'], 'verbose_name_plural': 'repositories'},
        ),
    ]
