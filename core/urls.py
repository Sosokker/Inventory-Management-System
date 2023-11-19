from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('inventory.urls'), name='dashboard'),
    path('', include('transaction.urls'), name='transaction'),
    path('', RedirectView.as_view(url='/overview/')),
]
