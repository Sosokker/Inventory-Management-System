from django.urls import path, include
from inventory.views import OverviewView, WarehouseView, InventoryView, WarehouseDetailView

urlpatterns = [
    path('overview/', OverviewView.as_view(), name='overview'),
    path('warehouse/', WarehouseView.as_view(), name='warehouse'),
    path('warehouse/<int:id>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
    path('warehouse/<int:wid>/<int:iid>/', InventoryView.as_view(), name='inventory'),
]
