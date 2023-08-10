from django.contrib import admin
from pizzas.models import Pizza, Topping

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)