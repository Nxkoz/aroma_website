from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                order.items.create(
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/order_created.html', {'order': order})
        else:
            # если форма невалидна — просто возвращаем её с ошибками:
            return render(request, 'orders/order_create.html', {
                'form': form,
                'error_message': 'Будь ласка, виправте помилки у формі.'
            })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'form': form})