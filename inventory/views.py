from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.views import FilterView
from inventory.filters import WarehouseFilter, InventoryFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from inventory.models import Warehouse, Inventory
from inventory.utils import stock_percentage_all, count_pending_supply
from transaction.models import Customer

@login_required
def Over(request):
    return render(request, 'inventory/index.html')

class OverviewView(TemplateView, LoginRequiredMixin):
    template_name = "inventory/overview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warehouse_list'] = Warehouse.objects.all()
        context['warehouse_count'] = Warehouse.objects.count()
        context['customer_count'] = Customer.objects.count()
        context['stock_percentage'] = stock_percentage_all()
        context['pending_supply'] = count_pending_supply()
        return context
    

class WarehouseView(FilterView, LoginRequiredMixin):
    model = Warehouse
    template_name = "inventory/warehouse.html"
    filterset_class = WarehouseFilter

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['warehouse_list'] = Warehouse.objects.all()
        return context
    

class WarehouseDetailView(FilterView, LoginRequiredMixin):
    model = Inventory
    template_name = "inventory/warehouse_detail.html"
    filterset_class = InventoryFilter
    context_object_name = 'inventory_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warehouse_id'] = self.kwargs.get('id')
        context['inventory_list'] = Inventory.objects.all()
        return context


class InventoryView(TemplateView, LoginRequiredMixin):
    template_name = "inventory/inventory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warehouse_list'] = Warehouse.objects.all()
        return context