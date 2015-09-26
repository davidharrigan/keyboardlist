# -*- coding: utf-8 -*-

import logging
import pymongo

from scrapy.conf import settings

logger = logging.getLogger(__name__)


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]

    def select_collection(self, spider):
        if spider.name == 'mechanicalkeyboards.com':
            self.collection = self.db['mechanicalkeyboards']
        else:
            raise Exception("Pipeline not implemented for {}".format(spider.name))

    def process_item(self, item, spider):
        self.select_collection(spider)
        if item:
            self.collection.insert(dict(item))
            logger.info("Keyboard added to database!")
        return item
