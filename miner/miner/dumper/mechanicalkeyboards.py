import logging
from . import base

logger = logging.getLogger(__name__)


class MechanicalKeyboardDumper(base.Dumper):
    def __init__(self):
        self.collection = self.db['mechanicalkeyboards']

    def dump(self):
        for record in self.collection.find():
            logger.info('Processing {}, page #{}'.format(record['_id'], record['page']))
            self.send(manufacturer=record.get('manufacturer'), model=record.get('model'),
                      switch_type=record.get('switch_type'), size=record.get('size'),
                      led='backlit_led' in record, seller='MechanicalKeyboards.com',
                      price=record.get('price'), url=record.get('url'),
                      stock=record.get('stock', 'Out of Stock'))

if __name__ == '__main__':
    dumper = MechanicalKeyboardDumper()
    dumper.dump()
