# Generated by Django 4.1.7 on 2023-04-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0016_alter_repository_image_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
