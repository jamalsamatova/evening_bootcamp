from django.urls import path

from applications.author.views import AuthorListView

urlpatterns = [
    path('author/', AuthorListView.as_views()),
]