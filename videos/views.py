from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Videos
from .serializers import Videoserializers


class Videolist(ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers


class Videodetail(RetrieveAPIView):
    queryset = Videos.objects.all()
    serializer_class = Videoserializers
