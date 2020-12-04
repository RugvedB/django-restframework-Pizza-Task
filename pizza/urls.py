from django.urls import path, include
from .views import *

urlpatterns = [
    path("pizzas/", PizzaList.as_view()),
    path("pizzas/create", PizzaCreate.as_view()),
    path("pizzas/list", PizzaListAll.as_view()),
    path("pizzas/retrieve/<str:id>", PizzaRetrieve.as_view()),
    path("pizzas/update/<str:id>", PizzaUpdate.as_view()),
    path("pizzas/destroy/<str:id>", PizzaDestroy.as_view()),
    
    
    path("toppings/", ToppingList.as_view()),
    
]