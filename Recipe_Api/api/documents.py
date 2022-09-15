# from dataclasses import fields
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Recipe

@registry.register_document
class RecipeDocument(Document):

    class Index:
        name = 'r_recipe'

    class Django:
        model = Recipe
        fields = [
            'name',
            'labels',
            "ingredients",
            'steps'
        ]
