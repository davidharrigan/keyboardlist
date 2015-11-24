from rest_framework import serializers

from .models import Seller, KeyboardInventory


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('id', 'name', 'domain')


class KeyboardInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyboardInventory
        fields = ('price', 'url', 'switch_type', 'stock', 'seller', 'keyboard')
