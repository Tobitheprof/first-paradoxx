# Generated by Django 4.0 on 2023-01-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradox', '0002_slide_rename_username_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(null=True),
        ),
    ]
