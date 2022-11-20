from django.test import TestCase

from stripe_app.items.models import Item
from stripe_app.orders.models import Order, ItemOrder, Discount, Tax
from stripe_app.tests.utils import get_test_data


class ModelTest(TestCase):

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

    def test_objects_creation(self):
        self.assertTrue(isinstance(self.item, Item))
        self.assertEqual(
            self.item.name,
            self.test_data_items['items']['item1']['name']
        )
        self.assertEqual(
            self.item.description,
            self.test_data_items['items']['item1']['description']
        )
        self.assertEqual(
            self.item.price,
            self.test_data_items['items']['item1']['price']
        )

        self.assertTrue(isinstance(self.order, Order))
        self.assertEqual(
            self.order.discount,
            self.discount
        )
        self.assertEqual(
            self.order.tax,
            self.tax
        )
        for itemorder in self.order.itemorder.get_queryset():
            self.assertEqual(
                itemorder.quantity,
                self.quantity
            )
            self.assertEqual(
                itemorder.item,
                self.item
            )
