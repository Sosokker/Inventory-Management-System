from django.urls import path

from transaction.views import CustomerOrderView

urlpatterns = [
    path('order/', CustomerOrderView.as_view(), name='customer-order'),
]
