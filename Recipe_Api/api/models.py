
from elasticsearch_dsl import Object, Nested
from django.db import models

# Create your models here.
"""
class Ingredients(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=500)
"""

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    labels = models.CharField(max_length=100, default="null")
    ingredients = models.CharField(max_length=100, default="null")
    recipe_steps = models.CharField(max_length=100, default="null")




    