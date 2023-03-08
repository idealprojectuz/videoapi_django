from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Videodetail, Videolist, Videoapi, VideoCreate
urlpatterns = [
    # path('<int:pk>/', Videodetail.as_view()),
    path('v2/', Videolist.as_view()),
    path('v2/<int:pk>', Videoapi.as_view()),
    path('v2/create', VideoCreate.as_view()),
]
