from rest_framework.generics import ListAPIView

from applications.author.models import Author
from applications.author.serializers import AuthorSerializer


class AuthorListView(ListAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
