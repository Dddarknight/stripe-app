import os
import stripe
from django.shortcuts import redirect
from django.views import View, generic

from stripe_app.orders.models import Order


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
HOST = os.getenv('HOST')


class StripeSessionOrderView(View):

    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        line_items = []
        for element in order.itemorder.get_queryset():
            # currency = stripe.Payout.create(
            #     amount=1000, currency=element.item.currency)
            item_data = {
                'price_data': {
                    'currency': 'usd',#element.item.currency,
                    'product_data': {
                        'name': element.item.name,
                    },
                    'unit_amount': element.item.price,
                },
                'quantity': element.quantity,  
            }
            if order.tax:
                tax_rate = stripe.TaxRate.create(
                    display_name=order.tax.name,
                    percentage=order.tax.rate,
                    inclusive=False
                )
                item_data.update(
                    {'tax_rates': [tax_rate.id]})
            line_items.append(item_data)

        session_kwargs = {
            'payment_method_types': ['card'],
            'line_items': line_items,
            'mode': 'payment',
            'success_url': f"{HOST}/success",
            'cancel_url': f"{HOST}/cancel",
        }
        if order.discount:
            coupon = stripe.Coupon.create(
                percent_off=order.discount.discount,
                duration="once",
            )
            session_kwargs.update(
                {'discounts': [{'coupon': coupon.id}]})
        session = stripe.checkout.Session.create(**session_kwargs)
        return redirect(session.url)


class BuyOrderView(generic.TemplateView):
    template_name = 'orders/buy-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(id=kwargs['pk'])
        itemorders = order.itemorder.get_queryset()
        context['order'] = order
        context['itemorders'] = itemorders
        return context
