from django.shortcuts import render, get_object_or_404
from .models import Hoodie
from cart.forms import CartAddProductForm

def product_list(request):
    products = Hoodie.objects.all()
    return render(request,
                  'products/product_list.html',
                  {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Hoodie,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'products/product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form},)