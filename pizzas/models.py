from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=25)

class Topping(models.Model):
    topping_name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza)
