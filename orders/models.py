from django.db import models, transaction
from decimal import Decimal
from django.conf import settings
from decouple import config
from wallets.models import Wallet


# Read the 'PRICE' environment variable
crypto_price = config('DEFAULT_CURRENCY_PRICE', cast=float)


class PurchaseOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    cryptocurrency_symbol = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=crypto_price)
    completed = models.BooleanField(default=False)

    @classmethod
    @transaction.atomic
    def create_purchase_order(cls, user, amount, cryptocurrency_symbol=config('CRYPTO_SYMBOL')):
        price = Decimal(amount) * Decimal(crypto_price)
        # Create a new purchase order
        order = cls.objects.create(
            user=user,
            cryptocurrency_symbol=cryptocurrency_symbol,
            amount=amount,
            price=price
        )

        # decrease the price from the user's wallet
        Wallet.objects.filter(user=user).first().withdraw(amount=price)
        
        if price > 10.0:
            cls.buy_from_exchange(order, price)
        return order

    @classmethod
    def buy_from_exchange(cls, orders, amount):
        # Make the request to international exchanges
        # import requests
        # response = requests.post('exchange_api_url', data={'symbol': symbol, 'amount': amount})
        if True:
            cls.update_order(orders, {'completed': True})

    @classmethod
    def update_order(cls, orders, fields):
        if isinstance(orders, cls):
            # If 'orders' is a single instance, update it directly
            with transaction.atomic():
                orders = cls.objects.filter(pk=orders.pk).select_for_update()
                orders.update(**fields)
        elif isinstance(orders, models.query.QuerySet):
            # If 'orders' is a queryset, update all instances in the queryset
            with transaction.atomic():
                orders = orders.select_for_update()
                orders.update(**fields)
        else:
            raise ValueError("Invalid 'orders' argument")

        return orders
