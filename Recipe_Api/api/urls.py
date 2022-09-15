from django.urls import path
from .views import RecipeView, RecipeSearch, RecipeUpdate, RecipeNew



urlpatterns = [
    path('new/', RecipeNew.as_view(), name='balance_account'),
    path('view/', RecipeView.as_view(), name='balance_account'),
    path('search/', RecipeSearch.as_view(), name='balance_account'),
    path('update/', RecipeUpdate.as_view(), name='balance_account'),
]