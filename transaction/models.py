from django.db import models

from inventory.models import Warehouse, Item

class Supplier(models.Model):
    """
    The one who supply the item to the warehouse

    :param name: Name of the supplier
    :param address: Address of the supplier
    """
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.address}"

class Supply(models.Model):
    """
    Supply is a transaction that the supplier supply the item to the warehouse

    :param supplier: Supplier that supply the item
    :param item: Item that is supplied
    :param quantity: Quantity of the item
    :param arrive_date: Date that the item arrive the warehouse
    """
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    arrive_date = models.DateField()

    def __str__(self):
        return f"{self.supplier.name} - {self.item.name} - {self.quantity}"

    class Meta:
        verbose_name_plural = 'Supplies'


class Customer(models.Model):
    """
    Customer is the one who buy the item from the warehouse

    :param name: Name of the customer
    :param address: Address of the customer
    """
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.address}"

class Order(models.Model):
    """
    Order is a transaction that the customer buy the item from the warehouse

    :param customer: Customer that buy the item
    :param item: Item that is bought
    :param order_date: Date that the item is bought
    :param quantity: Quantity of the item
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customer.name} - {self.item.name} - {self.quantity}"

class Transfer(models.Model):
    """
    Transfer is a transaction that the item is transfered from one warehouse to another

    :param from_warehouse: Warehouse that the item is transfered from
    :param to_warehouse: Warehouse that the item is transfered to
    :param item: Item that is transfered
    :param quantity: Quantity of the item
    :param from_date_timestamp: Date that the item is transfered from the warehouse
    :param to_date_timestamp: Date that the item arrive new warehouse
    """
    from_warehouse = models.ForeignKey(Warehouse, related_name='transfer_from', on_delete=models.CASCADE)
    to_warehouse = models.ForeignKey(Warehouse, related_name='transfer_to', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    from_date_timestamp = models.DateTimeField()
    to_date_timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.from_warehouse.name} - {self.to_warehouse.name} - {self.item.name} - {self.quantity}"