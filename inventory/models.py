from django.db import models


class Warehouse(models.Model):
    """
    Warehouse is a place where items are stored.

    :param name: Name of the warehouse
    :param address: Address of the warehouse
    :param have_freeze: Whether the warehouse have freezer or not
    """
    name = models.CharField(max_length=255)
    address = models.TextField()
    have_freeze = models.BooleanField()

    @property
    def stock_percentage(self) -> float:
        inventories = Inventory.objects.filter(warehouse=self)
        total_stock = 0
        total_max_stock = 0
        for inventory in inventories:
            total_stock += inventory.current_stock
            total_max_stock += inventory.max_stock
        return total_stock / total_max_stock * 100

    @property
    def inventory_count(self) -> int:
        return Inventory.objects.filter(warehouse=self).count()

    def __str__(self):
        return f"{self.name}"

class Inventory(models.Model):
    """
    Inventory is in warehouse, It can be a shelf, a room, a container etc.

    :param warehouse: Warehouse that the inventory belongs to
    :param max_stock: Maximum stock of the inventory
    :param min_stock: Minimum stock of the inventory
    :param current_stock: Current stock of the inventory
    """
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    max_stock = models.IntegerField()
    min_stock = models.IntegerField(default=0)
    current_stock = models.IntegerField(default=0)

    @property
    def stock_percentage(self) -> float:
        return self.current_stock / self.max_stock * 100

    @property
    def stock_identifier(self) -> str:
        return f"#{self.id} {self.warehouse.name}"

    def __str__(self):
        return f"{self.warehouse.name} - {self.stock_percentage}%"

    class Meta:
        verbose_name_plural = 'Inventories'


class Item(models.Model):
    """
    Item such as food, drink, furnoture etc.

    :param inventory: Inventory that the item belongs to
    :param name: Name of the item
    :param description: Description of the item
    :param category: Category of the item
    :param weight: Weight of the item in kg
    :param quantity: Quantity of the item
    """
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.quantity}"