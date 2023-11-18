from django.contrib import admin
from transaction.models import Supplier, Supply, Customer, Order, Transfer


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'item', 'quantity', 'arrive_date')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'order_date', 'quantity')

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('from_warehouse', 'to_warehouse', 'item', 'from_date_timestamp', 'to_date_timestamp', 'quantity')