# -*- coding: utf-8 -*-
import scrapy


class KeyboardItem(scrapy.Item):
    model = scrapy.Field()
    size = scrapy.Field()
    manufacturer = scrapy.Field()
    switch_type = scrapy.Field()
    usb_key_rollover = scrapy.Field()
    ps2_key_rollover = scrapy.Field()
    backlit_led = scrapy.Field()
    special_key_led = scrapy.Field()
    multimedia_keys = scrapy.Field()
    built_in_usb_ports = scrapy.Field()
    built_in_audio_port = scrapy.Field()
    built_in_mic_port = scrapy.Field()
    keycap_plastic = scrapy.Field()
    keycap_color = scrapy.Field()
    key_print_method = scrapy.Field()
    key_print_color = scrapy.Field()
    key_print_position = scrapy.Field()
    key_print_size = scrapy.Field()
    switch_mount_type = scrapy.Field()
    weight = scrapy.Field()
    dimensions = scrapy.Field()
    interface = scrapy.Field()
    domain = scrapy.Field()
    url = scrapy.Field()
