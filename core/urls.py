from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('dashboard/', include('inventory.urls'), name='dashboard'),
    path('', RedirectView.as_view(url='/dashboard/overview/')),
]
