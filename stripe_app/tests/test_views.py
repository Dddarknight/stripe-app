from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy

from stripe_app.items.models import Item
from stripe_app.orders.models import Order, ItemOrder, Discount, Tax
from stripe_app.tests.utils import get_test_data


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_data_items = get_test_data('items.json')
        cls.item = Item.objects.create(
            name=cls.test_data_items['items']['item1']['name'],
            description=cls.test_data_items['items']['item1']['description'],
            price=cls.test_data_items['items']['item1']['price']
        )
        cls.discount = Discount.objects.create(
            discount=20
        )
        cls.tax = Tax.objects.create(
            name='Sales',
            rate=30
        )
        cls.order = Order.objects.create(
            discount=cls.discount,
            tax=cls.tax
        )
        cls.quantity = 20
        ItemOrder.objects.create(
            order=cls.order,
            item=cls.item,
            quantity=cls.quantity
        )

    def test_item_view(self):
        c = Client()
        id = self.item.id
        response = c.get(reverse_lazy('item', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/buy-item.html')
        self.assertContains(response, self.item.name)
        self.assertContains(response, self.item.description)
        self.assertContains(response, self.item.price)

    def test_order_view(self):
        c = Client()
        id = self.order.id
        response = c.get(reverse_lazy('order', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/buy-order.html')
        self.assertContains(response, self.item.name)
        self.assertContains(response, self.item.price)
        self.assertContains(response, self.discount.discount)
        self.assertContains(response, self.tax.rate)
        self.assertContains(response, self.quantity)
