import logging

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Keyboard, Manufacturer
from .serializers import KeyboardSerializer, ManufacturerSerializer

logger = logging.getLogger('keyboardlist')


class KeyboardViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    serializer_class = KeyboardSerializer
    pagination_class = PageNumberPagination
    order_by_default = 'model'

    def get_queryset(self):
        logger.debug(self.request.query_params)
        sort_order = self.request.query_params.get('sort', self.order_by_default)
        manufacturer_id = self.request.query_params.get('manufacturer-id')
        queryset = Keyboard.objects.all().order_by(sort_order)
        if manufacturer_id:
            queryset = queryset.filter(manufacturer_id=manufacturer_id)
        logger.debug(queryset)
        return queryset


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'manufacturer'
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
