from django.db import models, transaction
from django.conf import settings
from .managers import WalletManager
from decimal import Decimal


class InsufficientBalanceError(Exception):
    pass


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(blank=True, null=True)

    objects = WalletManager()

    def __str__(self):
        return str(self.balance)

    def get_queryset(self):
        return self.__class__.objects.filter(id=self.id)

    @transaction.atomic
    def deposit(self, amount):
        obj = self.get_queryset().select_for_update().get()
        obj.balance += Decimal(amount)
        obj.save()
        return obj

    @transaction.atomic
    def withdraw(self, amount):
        obj = self.get_queryset().select_for_update().get()
        if Decimal(amount) > obj.balance:
            raise InsufficientBalanceError(
                "Insufficient balance to make the withdrawal")
        obj.balance -= Decimal(amount)
        obj.save()
        return obj
