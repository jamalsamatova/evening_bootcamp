from rest_framework import serializers

from applications.books.models import Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

