from django.db import models


class WalletManager(models.Manager):
    def create_wallet(self, user, initial_balance=0.00):
        wallet = self.create(user=user, balance=initial_balance)
        return wallet
