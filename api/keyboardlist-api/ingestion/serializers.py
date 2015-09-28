from rest_framework import serializers


class DataIngestionSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=255)
    keyboard_model = serializers.CharField(max_length=255)
    keyboard_switch_type = serializers.CharField(max_length=255)
    keyboard_size = serializers.CharField(max_length=255)
    keyboard_led = serializers.BooleanField()
    seller_name = serializers.CharField(max_length=255)
    seller_price = serializers.CharField(max_length=255)
    seller_url = serializers.URLField()
    seller_in_stock = serializers.CharField(max_length=255)
