from django.db import models
from django.core.validators import FileExtensionValidator
from categories.models import Categories


def validate_file_size(value):
    filesize = value.size
    if filesize > 500 * 1024 * 1024:  # 500 MB
        raise ValidationError(
            "The maximum file size that can be uploaded is 500 MB.")


class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    video_thumbnail = models.ImageField(
        upload_to='thumbnail/'
    )
    video = models.FileField(
        upload_to='videofiles/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv']),
            validate_file_size,
        ]
    )

    def __str__(self):
        return self.title

# Create your models here.
