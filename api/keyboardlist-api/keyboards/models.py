from django.db import models


class Manufacturer(models.Models):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)


class Keyboard(models.Model):
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

    model = models.CharField(max_length=255)
    switch_type = models.CharField(max_length=255, choices=SWITCH_TYPES)
    size = models.CharField(max_length=255, choices=KEYBOARD_SIZES)
    led = models.BooleanField(default=False)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True,
                                     on_delete=models.SET_NULL)
