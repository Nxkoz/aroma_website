from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/', views.payment_success, name='success'),
]