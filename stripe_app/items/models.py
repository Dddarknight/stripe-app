from django.db import models


class Item(models.Model):
    name = models.TextField(unique=True, max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    currency = models.TextField(max_length=3, default='usd')

    def __str__(self):
        return self.name
