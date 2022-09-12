# from dataclasses import fields
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Recipe

@registry.register_document
class RecipeDocement(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'recipe'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Recipe # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name'
        ]