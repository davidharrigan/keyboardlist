from rest_framework import serializers

from .models import Manufacturer, Keyboard


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'description', 'url')


class KeyboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyboard
        fields = ('model', 'switch_type', 'size', 'led', 'manufacturer')
