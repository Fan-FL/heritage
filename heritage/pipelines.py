# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json


class HeritagePipeline(object):

    def __init__(self):
        self.fileName = "data.json"
        with open(self.fileName, 'w', encoding='utf-8') as handle:
            pass

    def process_item(self, item, spider):
        # read item data
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # write file
        with open(self.fileName, 'a', encoding='utf-8') as handle:
            handle.write(line)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
