# Generated by Django 4.1.7 on 2023-03-14 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lithubs', '0007_remove_room_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
