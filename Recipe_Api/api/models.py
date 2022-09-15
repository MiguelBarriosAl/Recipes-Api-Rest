
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=10, default="null")
    labels = models.CharField(max_length=100, default="null")
    steps = models.CharField(max_length=100, default="null")