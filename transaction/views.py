from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from transaction.models import Order, Customer
from transaction.filters import OrderFilter

class CustomerOrderView(FilterView, LoginRequiredMixin):
    template_name = 'transaction/order_filter.html'
    model = Order
    filterset_class = OrderFilter
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer__isnull=False)  # Exclude orders without a customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context