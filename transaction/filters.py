from django import forms
import django_filters
from transaction.models import Order

class OrderFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains', label='Customer Name')
    item_name = django_filters.CharFilter(field_name='item__name', lookup_expr='icontains', label='Item Name')
    order_date = django_filters.DateFilter(field_name='order_date', label='Order Date (YYYY-MM-DD)', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['customer_name', 'item_name', 'order_date']
