from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Videos
from .serializers import Videoserializers
from rest_framework import permissions

class Videolist(ListAPIView):
    # permissions_classes=(permissions.IsAuthenticatedOrReadOnly)
    
    permissions_classes=(permissions.IsAuthenticated,)

    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class Videodetail(RetrieveAPIView):
    # permissions_classes=[IsAuthenticated]
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class Videoapi(RetrieveUpdateDestroyAPIView):
    # permissions_classes=[IsAuthenticatedOrReadOnly]
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class VideoCreate(CreateAPIView):
    # permissions_classes=[IsAuthenticatedOrReadOnly]
    queryset = Videos.objects.all()
    serializer_class = Videoserializers
