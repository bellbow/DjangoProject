from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context ={'all_pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)

    toppings = Topping.objects.filter(pizza=pizza)

    context ={'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

def comment(request):
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzas')
    context = {'form': form}
    return render(request, 'pizzas/comment.html', context)