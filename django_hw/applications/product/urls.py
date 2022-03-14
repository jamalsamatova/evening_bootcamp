rom django.urls import path
from .views import MusicListView

urlpatterns = [
    path('music-list/', MusicListView.as_view()),
]
