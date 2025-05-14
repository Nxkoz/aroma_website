from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвище", max_length=50)
    email = models.EmailField("Email")
    address = models.CharField("Адреса", max_length=250)
    postal_code = models.CharField("Поштовий індекс", max_length=20)
    city = models.CharField("Місто", max_length=100, blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    created = models.DateTimeField("Дата створення", auto_now_add=True)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name="Товар"
    )
    price = models.DecimalField("Ціна", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Кількість", default=1)

    class Meta:
        verbose_name = "Товар у замовленні"
        verbose_name_plural = "Товари у замовленні"

    def __str__(self):
        return str(self.id)