from django.shortcuts import render
from django.http import HttpResponse

def cart_add(request):
    return render(request, 'cart/shopcart.html')
