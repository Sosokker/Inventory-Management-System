import django_filters
from inventory.models import Warehouse

class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'have_freeze']