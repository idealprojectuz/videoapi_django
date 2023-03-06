# Generated by Django 4.1.7 on 2023-03-06 21:49

import django.core.validators
from django.db import migrations, models
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videos_video_alter_videos_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to='videofiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']), videos.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_thumbnail',
            field=models.ImageField(upload_to='thumbnail/'),
        ),
    ]
