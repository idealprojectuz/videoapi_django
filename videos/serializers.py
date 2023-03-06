from rest_framework import serializers
from .models import Videos


class Videoserializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('id', 'title', 'description',
                  'category', 'video_thumbnail', 'video')
