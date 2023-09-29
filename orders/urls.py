from django.urls import path
from . import views

urlpatterns = [
    path('add_order/', views.PurchaseOrderViewSet.as_view({'post': 'create'}), name='add_order'),
]
