from django.urls import path, include
from inventory.views import test

urlpatterns = [
    path('overview/', test, name='overview'),
]
