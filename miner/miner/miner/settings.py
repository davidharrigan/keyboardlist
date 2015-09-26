# -*- coding: utf-8 -*-

BOT_NAME = 'miner'

SPIDER_MODULES = ['miner.spiders']
NEWSPIDER_MODULE = 'miner.spiders'

ITEM_PIPELINES = ['miner.pipelines.MongoDBPipeline', ]
MONGODB_SERVER = "miner_mongo_1"
MONGODB_PORT = 27017
MONGODB_DB = "keyboardlist"
MONGODB_COLLECTION = "mechanicalkeyboards"
