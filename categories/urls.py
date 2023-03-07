from .views import Categorylists, CreateCategoriy, CategoryUpdate
from django.urls import path

urlpatterns = [
    path('/', Categorylists.as_view()),
    path('/<int:pk>', CategoryUpdate.as_view()),
    path('/create/', CreateCategoriy.as_view())
]
