from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Videos
from .serializers import Videoserializers


class Videolist(ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class Videodetail(RetrieveAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class Videoapi(RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class VideoCreate(CreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers
