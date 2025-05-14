from django.urls import path
from .views import ProductListView, ProductDetailView, add_to_cart, home

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/add/<int:id>/', add_to_cart, name='add_to_cart'),
]
