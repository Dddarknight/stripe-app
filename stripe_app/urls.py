from django.contrib import admin
from django.urls import path, include

from stripe_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         views.IndexView.as_view(),
         name='index'),
    path('', include('stripe_app.items.urls')),
    path('', include('stripe_app.orders.urls')),
    path('success/',
         views.SuccessView.as_view(),
         name='success'),
    path('cancel/',
         views.CancelView.as_view(),
         name='cancel'),
]
