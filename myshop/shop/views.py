from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product/detail.html', {'product': product})

def index(request):
    return render(request, 'shop/index.html')


def home(request):
    return render(request, 'shop/home.html')

