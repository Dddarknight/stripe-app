from django.db import models

from stripe_app.items.models import Item


class Discount(models.Model):
    discount = models.IntegerField()


class Tax(models.Model):
    name = models.TextField(unique=True, max_length=50)
    rate = models.IntegerField()


class Order(models.Model):
    discount = models.ForeignKey(
        Discount,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )


class ItemOrder(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='itemorder')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
