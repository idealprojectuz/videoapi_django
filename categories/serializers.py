from rest_framework import serializers
from .models import Categories


class Catserializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title')
