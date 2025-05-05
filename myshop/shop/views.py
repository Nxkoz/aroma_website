from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from cart.cart import Cart
from .forms import ProductFilterForm  # создам этот фильтр позже
from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/product_list.html'
    context_object_name = 'products'
    paginate_by = 6  # Отображать по 6 товаров на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        aroma = self.request.GET.get('aroma')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if aroma:
            queryset = queryset.filter(aroma__icontains=aroma)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductFilterForm(self.request.GET)
        return context

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