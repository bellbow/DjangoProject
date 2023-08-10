from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=25)
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    topping_name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.topping_name