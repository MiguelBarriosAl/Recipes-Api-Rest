
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=10, default="null")
    labels = models.CharField(max_length=100, default="null")
    recipe_step = models.CharField(max_length=100, default="null")


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE
    )

class Reccipe_step(models.Model):
    step = models.IntegerField()
    recipe = models.ForeignKey(
        Recipe, related_name="steps", on_delete=models.CASCADE
    )