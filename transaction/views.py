from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from transaction.models import Order, Transfer
from transaction.filters import OrderFilter, TransferFilter

class CustomerOrderView(FilterView, LoginRequiredMixin):
    template_name = 'transaction/order.html'
    model = Order
    filterset_class = OrderFilter
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer__isnull=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context
    

class TransferListView(FilterView):
    template_name = 'transaction/transfer.html'
    model = Transfer
    filterset_class = TransferFilter
    context_object_name = 'transfers_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transfer_list'] = Transfer.objects.all()
        return context