# -*- coding: utf-8 -*-

import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        dir_path = 'img/%s (%s)' % (item['name'], item['location'])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_url']:
            yield Request(image_url, meta={'item': item, 'url': image_url})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.meta['url']
        index = item['image_url'].index(url) + 1

        sufix = url.split('/')[-1].split('.')[-1]
        imageFileName = str(index) + "." + sufix
        dir_path = 'img/%s (%s)' % (item['name'], item['location'])
        file_path = '%s/%s' % (dir_path, imageFileName)
        return file_path
