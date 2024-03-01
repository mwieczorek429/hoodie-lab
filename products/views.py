from django.shortcuts import render
from .models import Hoodie
# Create your views here.

def product_list(request):
    products = Hoodie.objects.all()
    return render(request, 'products/product_list.html', {'products': products})