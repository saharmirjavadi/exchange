from django.test import TestCase
from .models import PurchaseOrder
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import PurchaseOrder
from wallets.models import Wallet
from decimal import Decimal
from decouple import config

User = get_user_model()


class PurchaseOrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'password')
        self.wallet = Wallet.objects.filter(
            user=self.user).first().deposit(amount=100.00)
        self.crypto_symbol = "ABAN"
        self.amount = Decimal(3)

    def test_create_purchase_order(self):
        initial_balance = self.wallet.balance

        order = PurchaseOrder.create_purchase_order(
            user=self.user, amount=self.amount, cryptocurrency_symbol=self.crypto_symbol
        )
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.cryptocurrency_symbol, self.crypto_symbol)
        self.assertEqual(order.amount, self.amount)
        self.assertEqual(order.price, self.amount *
                         Decimal(config('DEFAULT_CURRENCY_PRICE', cast=float)))
        self.assertFalse(order.completed)

        # Check if the user's wallet balance was updated correctly
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.balance, initial_balance - order.price)

    def test_update_order(self):
        order = PurchaseOrder.create_purchase_order(
            user=self.user, amount=self.amount, cryptocurrency_symbol=self.crypto_symbol
        )

        PurchaseOrder.update_order(order, {'completed': True})

        # Check if the order was updated correctly
        updated_order = PurchaseOrder.objects.get(pk=order.pk)
        self.assertTrue(updated_order.completed)

    def test_buy_from_exchange(self):
        order = PurchaseOrder.create_purchase_order(
            user=self.user, amount=self.amount, cryptocurrency_symbol=self.crypto_symbol
        )

        PurchaseOrder.buy_from_exchange(order, order.price)

        # Check if the order was marked as completed
        updated_order = PurchaseOrder.objects.get(pk=order.pk)
        self.assertTrue(updated_order.completed)
