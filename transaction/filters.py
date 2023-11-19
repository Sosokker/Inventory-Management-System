from django import forms
import django_filters
from transaction.models import Order, Transfer, Supply

class OrderFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains', label='Customer Name')
    item_name = django_filters.CharFilter(field_name='item__name', lookup_expr='icontains', label='Item Name')
    order_date = django_filters.DateFilter(field_name='order_date', label='Order Date (YYYY-MM-DD)', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['customer_name', 'item_name', 'order_date']


class TransferFilter(django_filters.FilterSet):
    from_warehouse = django_filters.CharFilter(field_name='from_warehouse__name', lookup_expr='icontains', label='From Warehouse')
    to_warehouse = django_filters.CharFilter(field_name='to_warehouse__name', lookup_expr='icontains', label='To Warehouse')
    item_name = django_filters.CharFilter(field_name='item__name', lookup_expr='icontains', label='Item Name')

    class Meta:
        model = Transfer
        fields = ['from_warehouse', 'to_warehouse', 'item_name']


class SupplyFilter(django_filters.FilterSet):
    supplier_name = django_filters.CharFilter(field_name='supplier__name', lookup_expr='icontains', label='Supplier Name')
    item_name = django_filters.CharFilter(field_name='item__name', lookup_expr='icontains', label='Item Name')

    class Meta:
        model = Supply
        fields = ['supplier_name', 'item_name']