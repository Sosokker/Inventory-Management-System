from django.urls import path

from transaction.views import CustomerOrderView, TransferListView

urlpatterns = [
    path('order/', CustomerOrderView.as_view(), name='customer-order'),
    path('transfers/', TransferListView.as_view(), name='transfer-list'),
]
