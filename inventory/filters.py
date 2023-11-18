import django_filters
from inventory.models import Warehouse, Inventory

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