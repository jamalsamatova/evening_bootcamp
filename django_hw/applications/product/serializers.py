from rest_framework import serializers

from applications.review.models import Category, Product


class CateogrySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ('name', 'slug')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
