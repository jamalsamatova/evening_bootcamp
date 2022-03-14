from rest_framework import viewsets
from applications.product.models import Product
from applications.product.serializers import ProductSerializer


class ProductListView(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer = ProductSerializer

    def create(self):
        pass

    def list(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


