from django.db import models

from keysboards.models import Keyboard


class Seller(models.Model):
    name = models.CharField(max_length=255)
    domain = models.URLField()


class KeyboardInventory(models.Model):
    STOCK = (
        ('out_of_stock', 'Out of Stock'),
        ('unknown', 'Unknown'),
        ('available', 'Available'),
    )

    price = models.IntegerField()
    url = models.URLField()
    switch_type = models.CharField(max_length=255)
    stock = models.CharField(max_length=50, choirces=STOCK)
    seller = models.ForeignKey(Seller)
    keyboard = models.ForeignKey(Keyboard)
