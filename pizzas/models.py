from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'pizzas'

    def __str__(self):
        return f'{self.name}, {self.description[:25]}...'


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return f'{self.name}'


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f'{self.pizza.name} topping'
