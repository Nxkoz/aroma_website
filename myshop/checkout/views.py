from django.shortcuts import render, redirect
from django.contrib import messages

def checkout_view(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')

        # Фейковая проверка
        if card_number and expiry and cvv:
            messages.success(request, 'Оплата пройшла успішно!')
            return redirect('checkout:success')
        else:
            messages.error(request, 'Будь ласка, заповніть усі поля.')

    return render(request, 'checkout/checkout.html')


def payment_success(request):
    return render(request, 'checkout/success.html')