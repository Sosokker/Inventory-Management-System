from django.contrib import admin
from inventory.models import Warehouse, Inventory, Item, Category

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'have_freeze')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('stock_identifier', 'warehouse', 'max_stock', 'min_stock', 'current_stock')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'weight', 'quantity', 'inventory')

@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('name',)