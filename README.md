# Api-Rest-Recipes

Development of Api Rest with Python in which you can create, retrieve, search or modify recipes. All the information will be stored in Elasticsearch.


# Elasticsearch

## Configuration

- INGEST NODE PIPELINES

        PUT _ingest/pipeline/add-current-time
        {
        "description" : "Date and time added when the document is indexed in Elasticsearch",
        "processors" : [
                {
                    "set": {
                        "field": "timestamp",
                        "value": "{{_ingest.timestamp}}"
                    }
                }
            ]
        }
    
- ILM POLIZY OF INDEX

        PUT _ilm/policy/recipes_policy
        {
        "policy": {
            "phases": {
            "hot": {
                "min_age": "0ms",
                "actions": {
                "rollover": {
                    "max_size": "50gb"
                },
                "set_priority": {
                    "priority": 100
                }
                }
            },
            "warm": {
                "min_age": "365d",
                "actions": {
                "forcemerge": {
                    "max_num_segments": 1
                },
                "set_priority": {
                    "priority": 50
                }
                }
            },
            "cold": {
                "min_age": "365d",
                "actions": {
                "set_priority": {
                    "priority": 0
                }
                }
            }
            }
        }
        }

- TEMPLATE OF INDEX

        PUT _template/recipe
        {
        "index_patterns": ["recipe-*"],
        "settings": {
            "index": {
            "lifecycle": {
                "name": "recipes_policy",
                "rollover_alias": "r_recipe"
            },
            "default_pipeline": "add-current-time",
            "mapping": {
                "nested_objects": {
                "limit": "10000"
                },
                "total_fields": {
                "limit": "10000"
                }
            },
            "number_of_shards": "3",
            "number_of_replicas": "1",
            "max_inner_result_window": "10000"
            }
        },
        "mappings" : {
            "dynamic_templates" : [ ],
            "properties" : {
                "ingredients" : {
                "type" : "nested",
                "properties": {
                    "quantity": {"type": "keyword"},
                    "ingredient": {"type": "text"}
                    }
                },
                "labels" : {
                "type" : "keyword"
                },
                "name" : {
                "type" : "text"
                },
                "recipe_steps" : {
                "type" : "nested",
                "properties": {
                    "step": {"type": "integer"},
                    "description": {"type": "text"}
                    }
                }
            }
            },
        "aliases": {}
        }

- STARTING INDEX ROLLOVER

        PUT recipe-000001
        {
            "aliases": {
                "r_recipe": {
                "is_write_index": true
                }
            }
        }