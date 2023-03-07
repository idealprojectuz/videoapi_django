from django.shortcuts import render
from .models import Categories
from .serializers import Catserializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class Categorylists(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = Catserializer


class CreateCategoriy(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = Catserializer


class CategoryUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = Catserializer
