from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Wallet, InsufficientBalanceError
from decimal import Decimal


User = get_user_model()


class WalletModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'password')
        self.wallet = Wallet.objects.filter(
            user=self.user).first().deposit(amount=100.00)

    def test_deposit(self):
        initial_balance = self.wallet.balance
        deposit_amount = 50.00
        self.wallet.deposit(deposit_amount)
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.balance,
                         initial_balance + Decimal(deposit_amount))

    def test_withdraw_sufficient_balance(self):
        initial_balance = self.wallet.balance
        withdraw_amount = 50.00
        self.wallet.withdraw(withdraw_amount)
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.balance,
                         initial_balance - Decimal(withdraw_amount))

    def test_withdraw_insufficient_balance(self):
        initial_balance = self.wallet.balance
        withdraw_amount = 150.00
        with self.assertRaises(InsufficientBalanceError):
            self.wallet.withdraw(withdraw_amount)
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.balance, initial_balance)
