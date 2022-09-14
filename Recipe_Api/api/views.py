import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe

class RecipeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        jd = json.loads(request.body)
        name_data = jd['name']
        labels = jd['labels']
        ingredients = jd['ingredients']
        recipe_steps = jd['recipe_steps']   
        recipe = Recipe(
            name=name_data,
            labels=labels,
            ingredients=ingredients,
            recipe_steps=recipe_steps
            )
        recipe.save()
        data = {"Message": "Success"}
    
        return JsonResponse(data)