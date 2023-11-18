from django.urls import path, include
from inventory.views import OverviewView, WarehouseView

urlpatterns = [
    path('overview/', OverviewView.as_view(), name='overview'),
    path('warehouse/', WarehouseView.as_view(), name='warehouse'),
]
