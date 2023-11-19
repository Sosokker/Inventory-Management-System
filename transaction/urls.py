from django.urls import path

from transaction.views import CustomerOrderView, TransferListView, SupplyListView

urlpatterns = [
    path('order/', CustomerOrderView.as_view(), name='customer-order'),
    path('transfers/', TransferListView.as_view(), name='transfer-list'),
    path('supply/', SupplyListView.as_view(), name='supply-list'),
]
