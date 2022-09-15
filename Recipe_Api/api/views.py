import json
from turtle import title
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from elasticsearch_dsl import Search, UpdateByQuery, Q
from elasticsearch import Elasticsearch
from .models import Recipe


class RecipeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            jd = json.loads(request.body)
            name_data = jd['name']
            labels = jd['labels']
            ingredient = jd['ingredients']
            recipe_step = jd['steps']         
            recipe = Recipe(
                name=name_data,
                labels=labels,
                ingredients=ingredient,
                steps=recipe_step
                )
            recipe.save()
            data = {"Message": "New Recipe Save"}
            return JsonResponse(data)
        except Exception as e:
            return HttpResponse(e, status=400)

    def get(self, request):
        try:
            jd = json.loads(request.body)
            name_data = jd['name']
            s = Search(index="r_recipe").query("match", name=name_data)
            search = s.execute()
            all_recipes = []
            for hit in search:
                data = {
                    "name" : hit.name,  
                    "labels" : hit.labels,
                    "ingredient" : hit.ingredient, 
                    "recipe_steps" : hit.recipe_steps}
                all_recipes.append(str(data))
            return JsonResponse(all_recipes, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)


class RecipeSearch(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        try:
            jd = json.loads(request.body)
            query = jd['term']
            s = Search(index="r_recipe").query("nested", path="ingredients", query=Q("match", **{"ingredients.ingredient": query}))
            search = s.execute()
            all_recipes = []
            for hit in search:
                print(hit)
                data = {
                    "name" : hit.name,  
                    "labels" : hit.labels,
                    "ingredients" : hit.ingredients, 
                    "steps" : hit.steps}
                all_recipes.append(str(data))
            return JsonResponse(all_recipes, safe=False)
        except Exception as e:
            return HttpResponse(e, status=400)  


class RecipeUpdate(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            field = jd['field']
            value = jd['value']
            query = str(jd['query'])
            path = "ctx._source.{}='{}'".format(field, value)
            print(path, query)
            s = UpdateByQuery(index="r_recipe").script(source=path).query("match", **{"name": query})
            search = s.execute()
            data = {"Message": "Update Saved"}
            return JsonResponse(data)
        except Exception as e:
            return HttpResponse(e, status=400)


