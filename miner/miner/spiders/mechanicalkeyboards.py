import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from miner.items import KeyboardItem


class MechanicalKeyboardSpider(Spider):
    name = 'mechanicalkeyboards.com'
    allowed_domains = ["mechanicalkeyboards.com"]

    def start_requests(self):
        start, end = 104, 1440
        url = 'https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p={}'
        for product in range(start, end):
            yield scrapy.Request(url.format(product), self.parse)

    def parse(self, response):
        web_page_to_field_mapping = {
            # General
            'Brand': 'manufacturer',
            'Size': 'size',
            'Model': 'model',

            # Specs
            'Switch Type': 'switch_type',
            'USB Key Rollover': 'usb_key_rollover',
            'PS/2 Key Rollover': 'ps2_key_rollover',
            'Backlit': 'backlit_led',
            'Special Key LEDs': 'special_key_led',
            'Multimedia Keys': 'multimedia_keys',
            'Built-in USB Ports': 'built_in_usb_ports',
            'Built-in Audio Port': 'built_in_audio_port',
            'Built-in Mic Port': 'built_in_mic_port',
            'Key Cap Plastic': 'keycap_plastic',
            'Key Print Method': 'key_print_method',
            'Key Cap Color': 'keycap_color',
            'Key Print Position': 'key_print_position',
            'Key Print Color': 'key_print_color',
            'Key Print Size': 'key_print_size',
            'Switch Mount Type': 'switch_mount_type',
            'Dimensions': 'dimensions',
            'Weight': 'weight',
            'Interface': 'interface'
        }

        extracted_data = {}
        spec_table_row = '//*[@class="spec_table"]/tr'
        specs = Selector(response).xpath(spec_table_row)
        for spec in specs:
            row = spec.xpath('td/text()').extract()
            if not row:
                continue
            description = row[0]
            if description in web_page_to_field_mapping and len(row) > 1:
                field_name = web_page_to_field_mapping[description]
                extracted_data[field_name] = row[1]

        domain = 'mechanicalkeyboards.com'
        url = response.url
        yield KeyboardItem(domain=domain, url=url, **extracted_data)

