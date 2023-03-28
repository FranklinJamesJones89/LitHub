# Generated by Django 4.1.7 on 2023-03-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithubs', '0006_alter_repository_body_alter_repository_form_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeRepository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='repository',
            name='num_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
