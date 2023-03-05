# Generated by Django 4.1.7 on 2023-03-03 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0005_repository_form_alter_repository_synopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
