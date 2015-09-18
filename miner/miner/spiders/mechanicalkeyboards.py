import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from miner.items import MechanicalKeyboardsItem


class MechanicalKeyboardSpider(Spider):
    name = 'mechanicalkeyboards.com'
    domain = 'mechanicalkeyboards.com'
    allowed_domains = ["mechanicalkeyboards.com"]
    current_page = 0
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

    def start_requests(self):
        start, end = 1, 2000
        url = 'https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p={}'
        for product in range(start, end):
            self.current_page = product
            yield scrapy.Request(url.format(product), self.parse)

    def does_product_exist(self, response):
        text = Selector(response).xpath('//*[@id="content"]/div[2]/p/text()').extract()
        if text and len(text) > 0:
            if 'This item is currently not available' in text[0]:
                self.logger.info('Item not avaiable for page {}'.format(self.current_page))
                return False
        return True

    def extract_price(self, response):
        price = Selector(response).xpath('//*[@id="product_price"]/text()').extract()
        if price and len(price) > 0:
            return price[0]

    def extract_stock(self, response):
        stock = Selector(response).xpath('//*[@id="content"]/div[2]/div[2]/div[1]/text()').extract()
        if stock and len(stock) > 2:
            return stock[3]

    def extract_specs(self, response):
        extracted_specs = {}
        spec_table_row = '//*[@class="spec_table"]/tr'
        specs = Selector(response).xpath(spec_table_row)
        for spec in specs:
            row = spec.xpath('td/text()').extract()
            if not row:
                continue
            description = row[0]
            if description in self.web_page_to_field_mapping and len(row) > 1:
                field_name = self.web_page_to_field_mapping[description]
                extracted_specs[field_name] = row[1]
        return extracted_specs

    def parse(self, response):
        if not self.does_product_exist(response):
            yield None
        else:
            extracted_data = {}
            extracted_data['price'] = self.extract_price(response)
            extracted_data['stock'] = self.extract_stock(response)
            extracted_data.update(self.extract_specs(response))
            url = response.url
            yield MechanicalKeyboardsItem(domain=self.domain, url=url, page=self.current_page, **extracted_data)
