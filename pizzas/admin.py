from django.contrib import admin
from pizzas.models import Pizza, Topping, Ingredient

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Ingredient)

