import pymongo

class ZhihuspiderPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        scrapy_db = client['zhihu']
        self.coll = scrapy_db['read']
     
    def process_item(self, item, spider):
        self.coll.insert_one(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
