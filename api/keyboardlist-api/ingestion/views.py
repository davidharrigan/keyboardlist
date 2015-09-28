import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DataIngestionSerializer
from keyboards.models import Manufacturer, Keyboard
from sellers.models import Seller, KeyboardInventory

logger = logging.getLogger(__name__)


class DataIngestionView(APIView):
    """
    Ingest keyboard listing information from miners into the API.

    TODO: authentication
    """
    def post(self, request, format=None):
        serializer = DataIngestionSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning('Serializer invalid: {}'.format(serializer.errors))
            return Response({'data_ingestion': 'error', 'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        self.process_serialized_data(serializer.validated_data)
        return Response({'data_ingestion': 'success'}, status=status.HTTP_200_OK)

    def process_serialized_data(self, data):
        manufacturer = Manufacturer.objects.get_or_create(name=data['manufacturer'])
        if manufacturer[1]:
            logger.info('Manufacturer Created: {}'.format(manufacturer[0]))
        seller = Seller.objects.get_or_create(name=data['seller_name'])
        keyboard = Keyboard.objects.get_or_create(
            model__iexact=data['keyboard_model'],
            manufacturer=manufacturer[0],
            led=data['keyboard_led'],
            normalize={
                'switch_type': data['keyboard_switch_type'],
                'size': data['keyboard_size']
            },
            defaults={
                'model': data['keyboard_model']
            }
        )
        keyboard_inventory = KeyboardInventory.objects.update_or_create(
            url=data['seller_url'],
            normalize={
                'price': data['seller_price'],
                'stock': data['seller_in_stock']
            },
            defaults={
                'switch_type': data['keyboard_switch_type'],
                'keyboard': keyboard[0],
                'seller': seller[0]
            }
        )
        logger.info('Manufacturer: {} | Seller: {} | Keyboard: {} | Inventory: {}'.format(
            manufacturer, seller, keyboard, keyboard_inventory))
