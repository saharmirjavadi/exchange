from django.contrib import admin
from .models import Wallet


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'updated_at')
    list_filter = ('user',)
    search_fields = ('user__username',)


admin.site.register(Wallet, UserWalletAdmin)
