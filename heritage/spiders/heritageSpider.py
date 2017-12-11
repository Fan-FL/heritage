# -*- coding: utf-8 -*-
import scrapy
from heritage.items import HeritageItem


class HeritageSpider(scrapy.Spider):
    name = "heritage"

    def __init__(self):
        self.allowed_domains = ["vhd.heritagecouncil.vic.gov.au"]
        self.start_urls = [
            'http://vhd.heritagecouncil.vic.gov.au/search?aut_off=1&aut%5B0%5D=&do=s&collapse=true&type=place&spage=1&tab=places&rpp=25&view=detailed&ppage=1']

    def parse(self, response):
        pageCount = response.xpath(
            './/ul[@class="pagination"]/li[last()-1]/a[1]/text()').extract()[0]
        yield scrapy.Request(url=self.start_urls[0],
                             callback=self.parseListPage)

        for page in range(2, int(pageCount) + 1):
            yield scrapy.Request(url="http://vhd.heritagecouncil.vic.gov.au/search?aut_off=1&aut%5B0%5D=&do=s&collapse=true&type=place&spage=1&tab=places&rpp=25&view=detailed&ppage=" + str(page), callback=self.parseListPage)

    def parseListPage(self, response):
        for box in response.xpath('//div[@class="display-control-places"]/ul[@class="search-results-listings"]/li[@class="row"]'):
            item = HeritageItem()
            item['name'] = box.xpath(
                './/div[@class="column col-name-details"]/p[@class="name"]/a/text()').extract()[0].replace('\n', '').strip()
            item['location'] = box.xpath(
                './/div[@class="column col-name-details"]/p[@class="location"]/text()').extract()[0]
            item['description'] = box.xpath(
                './/div[@class="column col-name-details"]/p[@class="description"]/text()').extract()[0]
            item['url'] = box.xpath(
                './/div[@class="column col-name-details"]/p[@class="name"]/a/@href').extract()[0]
            yield scrapy.Request(url=item['url'], meta={'item': item}, callback=self.parseHeritageLink)

    def parseHeritageLink(self, response):
        item = response.meta['item']
        content = ""
        for p in response.xpath('.//div[@class="content individual-listing-content"]/p[@class="c1"]/text()').extract():
            content = content + p + "\n\n"
        item['content'] = content
        item['image_url'] = response.xpath('//img[@class="gallery-image"]/@src').extract()
        yield item
