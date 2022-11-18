import os
import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View, generic

from stripe_app.items.models import Item


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
HOST = os.getenv('HOST')


class StripeSessionView(View):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['pk'])
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{HOST}/success",
            cancel_url=f"{HOST}/cancel",
        )
        return redirect(session.url)


class BuyItemView(generic.TemplateView):
    template_name = 'items/buy-item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(id=kwargs['pk'])
        context['item'] = item
        return context


class StripeIntentView(View):

    def get(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(id=kwargs['pk'])
            intent = stripe.PaymentIntent.create(
                amount=item.price,
                currency='usd',
                metadata={
                    "item_id": item.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})


class BuyItemIntentView(generic.TemplateView):
    template_name = 'items/buy-item-intent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(id=kwargs['pk'])
        context['item'] = item
        return context
