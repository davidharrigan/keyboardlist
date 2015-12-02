import logging
import sys

import pymongo
import requests

from miner import settings

# Log configuration
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__name__)

api_host = 'api_nginx_1'


class Dumper(object):
    api = 'http://{}/ingestion/'.format(api_host)
    client = pymongo.MongoClient(settings.MONGODB_SERVER, settings.MONGODB_PORT)
    db = client[settings.MONGODB_DB]
    session = requests.Session()

    def send(self, **kwargs):
        data = {
            'manufacturer': kwargs['manufacturer'],
            'keyboard_model': kwargs['model'],
            'keyboard_switch_type': kwargs['switch_type'],
            'keyboard_size': kwargs['size'],
            'keyboard_led': kwargs['led'],
            'seller_name': kwargs['seller'],
            'seller_price': kwargs['price'],
            'seller_url': kwargs['url'],
            'seller_in_stock': kwargs['stock'] or 'Out of Stock',
        }
        response = self.session.post(self.api, json=data, verify=False)
        logger.info('Response: {}'.format(response))
