from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    place_of_birth = models.CharField(max_length=30)

    def __str__(self):
        return self.name + self.last_name
