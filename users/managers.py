from django.contrib.auth.models import BaseUserManager
from wallets.models import Wallet


class UserManager(BaseUserManager):
    def create_user(self, username, mobile, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        if not mobile:
            raise ValueError('The Mobile field must be set')

        user = self.model(
            username=username,
            mobile=mobile,
        )

        user.set_password(password)
        user.save(using=self._db)
        Wallet.objects.create_wallet(user)
        return user

    def create_superuser(self, username, mobile, password=None):
        user = self.create_user(
            username=username,
            mobile=mobile,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
