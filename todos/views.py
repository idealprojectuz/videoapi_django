from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Todo
from .serializers import TodoSerializers

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers