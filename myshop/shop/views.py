from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from .models import Product
from cart.cart import Cart
from django.contrib import messages

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.all()
        # Сюда добавим фильтры позже
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=1)
    messages.success(request, f'Товар "{product.name}" додано в кошик!')
    return redirect('shop:product_detail', id=id)
