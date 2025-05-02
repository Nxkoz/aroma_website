from django.urls import path
from .views import ProductListView, ProductDetailView, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # Каталог
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),  # Детали товара
    path('cart/add/<int:id>/', add_to_cart, name='add_to_cart'),
]
