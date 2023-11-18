from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from inventory.models import Item
from transaction.models import Transfer


@receiver(pre_save, sender=Item)
def handle_item_move(sender, instance, **kwargs):
    """
    Signal to handle moving an Item to a new Inventory.
    """
    if instance.pk:
        old_item = Item.objects.get(pk=instance.pk)
        if old_item.inventory != instance.inventory:
            old_item.inventory.current_stock -= old_item.quantity
            old_item.inventory.save()

@receiver(post_save, sender=Item)
def update_inventory_current_stock(sender, instance, **kwargs):
    """
    Signal to update current_stock of related Inventory when an Item is created or assigned to a new Inventory.
    """
    if kwargs.get('created', False) or instance.pk:
        instance.inventory.current_stock += instance.quantity
        instance.inventory.save()


@receiver(post_save, sender=Item)
def create_transfer_instance(sender, instance, **kwargs):
    """
    Signal to create a Transfer instance when an Item is transferred between warehouses.
    """
    # If the item is being created or updated
    if kwargs.get('created', False) or instance.pk:
        if instance.pk and instance.inventory.warehouse != instance.inventory.old_warehouse:
            Transfer.objects.create(
                from_warehouse=instance.inventory.old_warehouse,
                to_warehouse=instance.inventory.warehouse,
                item=instance,
                quantity=instance.quantity,
            )