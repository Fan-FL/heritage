# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HeritageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    pass
