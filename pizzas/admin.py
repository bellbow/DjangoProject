from django.contrib import admin
from pizzas.models import Pizza, Topping, Comment

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Comment)