from django.shortcuts import render
from pizzas.models import Pizza, Topping, Ingredient


# Create your views here.
# path '/' - index
def index(request):
    return render(request, 'pizzas/index.html')


def menu(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}

    return render(request, 'pizzas/menu.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    description = pizza.description
    topping = Topping.objects.get(id=pizza_id)

    ingredients = Topping.objects.get(id=pizza_id).ingredients.all()

    context = {'pizza': pizza, 'description': description,
               'topping': topping, 'ingredients': ingredients}

    return render(request, 'pizzas/pizza.html', context)
