# Generated by Django 4.1.3 on 2023-08-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_user_image_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
