from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas =Pizza.objects.all()

    context ={'all_pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)
