from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація пройшла успішно! Ви увійшли в акаунт.')
            return redirect('home')  # или на другую нужную тебе страницу
    else:
        form = UserRegisterForm()

    # Указываем точный путь к шаблону
    return render(request, 'accounts/register.html', {'form': form})
