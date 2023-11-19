import django_filters
from django_filters import OrderingFilter
from inventory.models import Warehouse, Inventory, Item

class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'have_freeze']


class InventoryFilter(django_filters.FilterSet):
    current_stock__gte = django_filters.NumberFilter(field_name='current_stock', lookup_expr='gte', label='Min Current Stock')
    current_stock__lte = django_filters.NumberFilter(field_name='current_stock', lookup_expr='lte', label='Max Current Stock')
    max_stock__gte = django_filters.NumberFilter(field_name='max_stock', lookup_expr='gte', label='Min Max Stock')
    max_stock__lte = django_filters.NumberFilter(field_name='max_stock', lookup_expr='lte', label='Max Max Stock')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('current_stock', 'current_stock'),
            ('max_stock', 'max_stock'),
        ),
        field_labels={
            'current_stock': 'Current Stock',
            'max_stock': 'Max Stock',
        }
    )

    class Meta:
        model = Inventory
        fields = []


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Item Name')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains', label='Category')
    warehouse = django_filters.CharFilter(field_name='inventory__warehouse__name', lookup_expr='icontains', label='Warehouse')
    quantity = django_filters.NumberFilter(label='Quantity', widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'Range'}))
    weight = django_filters.NumberFilter(label='Weight', widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'Range'}))
    ordering = OrderingFilter(
        fields=(
            ('quantity', 'quantity'),
            ('weight', 'weight'),
            ('inventory__warehouse__name', 'warehouse_name'),
        ),
        field_labels={
            'quantity': 'Quantity',
            'weight': 'Weight',
            'inventory__warehouse__name': 'Warehouse Name',
        }
    )

    class Meta:
        model = Item
        fields = ['name', 'category', 'warehouse', 'quantity', 'weight']
