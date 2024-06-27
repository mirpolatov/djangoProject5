from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(Category, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # Ensure this is correct

    def __str__(self):
        return self.name
