import os
import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View, generic

from stripe_app.items.models import Item


HOST = os.getenv('HOST')


class StripeSessionView(View):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['pk'])
        secret_key = os.getenv('STRIPE_SECRET_KEY_USD') if (
            item.currency == 'usd') else os.getenv(
                'STRIPE_SECRET_KEY_ANOTHER_CURRENCY')
        stripe.api_key = secret_key
        product = stripe.Product.create(
            name=item.name,
            description=item.description,
        )
        price = stripe.Price.create(
            currency=item.currency,
            unit_amount=item.price,
            product=product,
        )
        item_data = {
            'price': price.id,
            'quantity': 1,
        }
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[item_data],
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
        publish_key = os.getenv('STRIPE_PUBLISH_KEY_USD') if (
            item.currency == 'usd') else os.getenv(
                'STRIPE_PUBLISH_KEY_ANOTHER_CURRENCY')
        context['STRIPE_PUBLISH_KEY'] = publish_key
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


class ItemsView(generic.ListView):
    template_name = 'items/items.html'
    model = Item
