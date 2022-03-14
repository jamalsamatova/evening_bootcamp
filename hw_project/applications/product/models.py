from django.db import models
from applications.product.utils import slug_generator


class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True, blank=True)
    price = models.IntegerField(blank=True)
    in_stock = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):
        slug = slug_generator(self.title)

    def __str__(self):
        return self.title
