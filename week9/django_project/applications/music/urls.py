from django.urls import path

from applications.music.views import SongsListView

urlpatterns = [
    path('songs-list/', SongsListView.as_view()),
]
