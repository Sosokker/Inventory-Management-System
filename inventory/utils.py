from inventory.models import Inventory
from transaction.models import Supply

def stock_percentage_all() -> float:
    inventories = Inventory.objects.all()
    total_stock = 0
    total_max_stock = 0
    for inventory in inventories:
        total_stock += inventory.current_stock
        total_max_stock += inventory.max_stock
    if total_max_stock == 0:
        return 0
    return total_stock / total_max_stock * 100


def count_pending_supply() -> int:
    pending_count = 0
    for supply in Supply.objects.all():
        if supply.pending_status():
            pending_count += 1
    return pending_count