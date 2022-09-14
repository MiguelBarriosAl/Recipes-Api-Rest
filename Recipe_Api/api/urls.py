from django.urls import path
from .views import RecipeView, RecipeSearch, RecipeUpdate



urlpatterns = [
    path('new/', RecipeView.as_view(), name='balance_account'),
    path('search/', RecipeSearch.as_view(), name='balance_account'),
    path('update/', RecipeUpdate.as_view(), name='balance_account'),
]