from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, primary_key=True)


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    price = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
