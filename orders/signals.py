from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from django.db.models import Sum


@receiver(post_save, sender=PurchaseOrder)
def check_order_price(sender, instance, created, **kwargs):
    if created and instance.price < 10.0 :
        # Check and calculate the total price of uncompleted orders
        uncompleted_orders = PurchaseOrder.objects.filter(completed=False,
                                                          cryptocurrency_symbol=instance.cryptocurrency_symbol)
        total_uncompleted_price = uncompleted_orders.aggregate(Sum('price'))['price__sum']
        if total_uncompleted_price is not None and total_uncompleted_price > 10.0:
            # Perform additional actions here for uncompleted orders with total price > $10
            instance.buy_from_exchange(uncompleted_orders, total_uncompleted_price)