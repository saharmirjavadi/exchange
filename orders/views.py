from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cryptocurrency_symbol = serializer.validated_data.get('cryptocurrency_symbol')
        amount = serializer.validated_data.get('amount')

        order = PurchaseOrder.create_purchase_order(
            user=request.user,
            amount=amount,
            cryptocurrency_symbol=cryptocurrency_symbol
        )

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
