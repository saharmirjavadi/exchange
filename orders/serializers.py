from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['amount', 'cryptocurrency_symbol']
