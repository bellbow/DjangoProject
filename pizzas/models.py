from django.db import models
from .models import *

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=25)
    pizza_image = models.ImageField(upload_to='pizzas/media', blank=True)
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    topping_name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.topping_name
    
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    pizza = models.ForeignKey(Pizza, on_delete= models.CASCADE)
    def __str__(self):
        return self.comment
    