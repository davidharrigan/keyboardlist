import re
import logging

from django.db import models

from keyboards.models import Keyboard
from .exceptions import NormalizePriceException

logger = logging.getLogger(__name__)

STOCK = (
    ('out_of_stock', 'Out of Stock'),
    ('unknown', 'Unknown'),
    ('available', 'Available'),
)


class Seller(models.Model):
    name = models.CharField(max_length=255)
    domain = models.URLField()

    def __str__(self):
        return self.name


class KeyboardInventoryQuerySet(models.query.QuerySet):
    """ Custom queryset for KeyboardInventory model """

    def update_or_create(self, defaults=None, normalize=None, **kwargs):
        """
        Overridden update_or_create to accept normalize argument. Values stored in normalize
        dictionary will be attempted to be normalized before being added to `defaults` dict.
        """
        if normalize is not None:
            defaults = defaults or {}
            defaults.update(**self.normalize_data(normalize))
        return super().update_or_create(defaults, **kwargs)

    def normalize_data(self, data):
        """
        Attempts to normalize given data. Valid options are `price` and `stock`.
        """
        normalized_data = {}
        if 'price' in data:
            normalized_data['price'] = self.normalize_price(data['price'])
        if 'stock' in data:
            normalized_data['stock'] = self.normalize_stock(data['stock'])
        return normalized_data

    def normalize_price(self, price):
        """
        Normalizes price into integer
        """
        try:
            return int(re.sub('[$,.\s]', '', price))
        except Exception as e:
            logger.error('Unable to normalize price: {} with exception: {}'.format(price, e))
            raise NormalizePriceException

    def normalize_stock(self, stock):
        """
        Normalize stock to match STOCK choice tuple defined above.
        """
        stock = re.sub('[,.+]', '', stock)
        valid_stock_types = [x[1] for x in STOCK]
        if stock.isdigit():
            if stock == "0":
                return "Out of Stock"
            if int(stock) > 0:
                return "Available"
        for valid_stock_type in valid_stock_types:
            if self.check_string_fragments_match(valid_stock_type, stock):
                return valid_stock_type
        return 'Unknown'

    def check_string_fragments_match(self, cmp1, cmp2):
        """
        This function will return True for the following conditions:
        - concatenated strings match
        - one of cmp1's fragments is in cmp2
        - one of cmp2's fragments is in cmp1
        """
        if self.check_case_insensitive_match(cmp1.replace(' ', ''), cmp2.replace(' ', '')):
            return True
        for fragment in cmp1.split():
            if fragment.lower() in cmp2.lower():
                return True
        for fragment in cmp2.split():
            if fragment.lower() in cmp1.lower():
                return True
        return False

    def check_case_insensitive_match(self, cmp1, cmp2):
        """
        Checks whether cmp1 and cmp2 match.
        """
        return cmp1.lower() == cmp2.lower()


class KeyboardInventoryManager(models.Manager):
    def get_queryset(self):
        return KeyboardInventoryQuerySet(self.model)


class KeyboardInventory(models.Model):
    price = models.IntegerField()
    url = models.URLField(unique=True)
    switch_type = models.CharField(max_length=255)
    stock = models.CharField(max_length=50, choices=STOCK)
    seller = models.ForeignKey(Seller)
    keyboard = models.ForeignKey(Keyboard)

    objects = KeyboardInventoryManager()

    def __str__(self):
        return self.url
