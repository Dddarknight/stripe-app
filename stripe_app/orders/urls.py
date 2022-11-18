from django.urls import path

from stripe_app.orders import views


urlpatterns = [
    path('buy-order/<int:pk>/',
         views.StripeSessionOrderView.as_view(),
         name='stripe-session-order'),
    path('order/<int:pk>/',
         views.BuyOrderView.as_view(),
         name='order'),
]
