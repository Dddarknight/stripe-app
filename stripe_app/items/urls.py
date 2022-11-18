from django.urls import path

from stripe_app.items import views


urlpatterns = [
    path('buy/<int:pk>/',
         views.StripeSessionView.as_view(),
         name='stripe-session'),
    path('item/<int:pk>/',
         views.BuyItemView.as_view(),
         name='item'),
    path('item-intent/<int:pk>/',
         views.StripeIntentView.as_view(),
         name='item-intent'),
    path('buy-item-intent/<int:pk>/',
         views.BuyItemIntentView.as_view(),
         name='buy-item-intent'),
]
