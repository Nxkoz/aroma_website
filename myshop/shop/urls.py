from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('catalog/', views.product_list, name='product_list'),  # Каталог
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Детали товара
]




