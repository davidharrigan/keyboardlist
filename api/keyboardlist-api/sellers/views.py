from rest_framework import viewsets

from .models import Seller, KeyboardInventory
from .serializers import SellerSerializer, KeyboardInventorySerializer


class SellerViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'seller'
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class KeyboardInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = KeyboardInventory.objects.all()
    serializer_class = KeyboardInventorySerializer
