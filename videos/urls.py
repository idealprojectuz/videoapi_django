from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Videodetail, Videolist
urlpatterns = [
    path('<int:pk>/', Videodetail.as_view()),
    path('', Videolist.as_view()),

]
