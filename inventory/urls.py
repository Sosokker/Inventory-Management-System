from django.urls import path, include
from inventory.views import OverviewView

urlpatterns = [
    path('overview/', OverviewView.as_view(), name='overview'),
]
