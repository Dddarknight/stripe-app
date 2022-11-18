from django.contrib import admin
from stripe_app.items.models import Item
from stripe_app.orders.models import Order, ItemOrder, Discount, Tax


admin.site.register(Item)
admin.site.register(Discount)
admin.site.register(Tax)
admin.site.register(Order)
admin.site.register(ItemOrder)
