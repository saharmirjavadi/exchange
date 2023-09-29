from django.contrib import admin
from .models import PurchaseOrder


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency_symbol',
                    'amount', 'price', 'completed')
    list_filter = ('user', 'completed')
    search_fields = ('user__username', 'cryptocurrency_symbol')


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
