from django.urls import path

from applications.books.views import BooksListView

urlpatterns = [
    path('books/', BooksListView.as_view())
]