from django.contrib import admin
from inventory.models import Warehouse, Inventory, Item

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'have_freeze')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('warehouse', 'max_stock', 'min_stock', 'current_stock')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'name', 'description', 'category', 'weight', 'quantity')