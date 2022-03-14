from rest_framework.generics import ListAPIView

from applications.books.models import Book
from applications.books.serializers import BooksSerializer


class BooksListView(ListAPIView):

    queryset = Book.objects_all()
    serializer_class = BooksSerializer


