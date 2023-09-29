from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=150)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mobile']

    def __str__(self):
        return self.username
