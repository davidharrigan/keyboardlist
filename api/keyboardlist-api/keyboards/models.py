"""
This module contains information about various keyboard manufacturers and keyboard models
"""
import logging
from django.db import models

logger = logging.getLogger(__name__)

SWITCH_TYPES = (
    ('alps', 'ALPS'),
    ('buckling_spring', 'Buckling Spring'),
    ('cherry', 'Cherry MX'),
    ('kalih', 'Kalih'),
    ('other', 'Other'),
)
KEYBOARD_SIZES = (
    ('tkl', 'Tenkeyless'),
    ('full', 'Full Size'),
    ('other', 'Other')
)


class Manufacturer(models.Model):
    """
    Model to store Keyboard manufacturer
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class KeyboardQuerySet(models.query.QuerySet):
    def get_or_create(self, defaults=None, normalize=None, **kwargs):
        """
        Overridden get_or_create to accept normalize argument.  Values stored in normalize
        dictionary will be attempted to be normalized before lookup and creation.
        """
        if normalize is not None:
            kwargs.update(**self.normalize_data(normalize))
            logger.debug('kwargs: {}'.format(kwargs))
        return super().get_or_create(defaults, **kwargs)

    def normalize_data(self, data):
        """
        Attempts to normalize given data. Valid options are 'switch_type' and 'size'.
        """
        normalized_data = {}
        if 'switch_type' in data:
            normalized_data['switch_type'] = self.normalize_switch_type(data['switch_type'])
        if 'size' in data:
            normalized_data['size'] = self.normalize_size(data['size'])
        return normalized_data

    def normalize_switch_type(self, switch_type):
        """
        Normalizes switch type to match SWITCH_TYPES choice tuple defined above.
        """
        valid_switch_types = [x[1] for x in SWITCH_TYPES]
        if switch_type in valid_switch_types:
            return switch_type  # Already valid
        for valid_switch_type in valid_switch_types:
            if self.check_string_fragments_match(valid_switch_type, switch_type):
                return valid_switch_type
        return 'Other'

    def normalize_size(self, size):
        """
        Normalizes size to match KEYBOARD_SIZES choice tuple defined above.
        """
        valid_sizes = [x[1] for x in KEYBOARD_SIZES]
        if size in valid_sizes:
            return size
        for valid_size in valid_sizes:
            if self.check_string_fragments_match(valid_size, size):
                return valid_size
        return 'Other'

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


class KeyboardManager(models.Manager):
    def get_queryset(self):
        return KeyboardQuerySet(self.model)


class Keyboard(models.Model):
    """
    Model to store keyboard models. Same model with various switch/LED configurations
    are considered different.
    """
    model = models.CharField(max_length=255)
    switch_type = models.CharField(max_length=255, choices=SWITCH_TYPES)
    size = models.CharField(max_length=255, choices=KEYBOARD_SIZES)
    led = models.BooleanField(default=False)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    objects = KeyboardManager()

    def __str__(self):
        return self.model
