from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from cart.cart import Cart
from django.contrib import messages



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

def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=1)
    messages.success(request, f'Товар "{product.name}" додано в кошик!')
    return redirect('shop:product_detail', id=id)
