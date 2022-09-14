# from dataclasses import fields
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Recipe, Ingredient, Reccipe_step


@registry.register_document
class RecipeDocument(Document):
    ingredients = fields.NestedField(properties={
        "name": fields.TextField(),
        "quantity" : fields.TextField()

    })

    steps = fields.NestedField(properties={
        "step": fields.IntegerField(),
        "description" : fields.TextField()

    })

    class Index:
        name = 'r_recipe'

    class Django:
        model = Recipe
        fields = [
            'name',
            'labels',
            "ingredient",
            'recipe_step'
        ]
        related_models = [Ingredient, Reccipe_step]

