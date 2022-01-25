from django.urls import path
from pizzas import views

app_name = 'pizzas'

urlpatterns = [
    # main page
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pizza_id>/', views.pizza, name='pizza'),
]
