from rest_framework import viewsets

from .models import Keyboard, Manufacturer
from .serializers import KeyboardSerializer, ManufacturerSerializer


class KeyboardViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'manufacturer'
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
