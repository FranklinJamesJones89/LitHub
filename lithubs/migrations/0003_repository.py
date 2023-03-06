# Generated by Django 4.1.7 on 2023-03-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('synopsis', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]