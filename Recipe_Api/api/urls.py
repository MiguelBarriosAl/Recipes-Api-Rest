from django.urls import path
from .views import RecipeView



urlpatterns = [
    path('new/', RecipeView.as_view(), name='balance_account'),
]