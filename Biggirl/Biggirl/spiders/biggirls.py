# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider,Rule
from Biggirl.items import BiggirlItem

class BiggirlsSpider(CrawlSpider):
    name = 'biggirls'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/mingxing/',
                  'http://www.mm131.com/qingchun/',
                  'http://www.mm131.com/xiaohua/',
                  'http://www.mm131.com/chemo/',
                  'http://www.mm131.com/qipao/',
                  'http://www.mm131.com/xinggan/',
                  ]

    def parse(self,response):
        colllist = response.xpath("//dl[@class='list-left public-box']")
        for collmessage in colllist:
            collname = collmessage.xpath(".//dd/a/img/@alt").extract()#合集名称
            collurl = collmessage.xpath(".//dd/a[@target='_blank']/@href").extract()#合集url
            print(collname,collurl)

            nextpage = collmessage.xpath("//a[contains(text(),'下一页')]/@href").extract_first()#下一页url
            if nextpage is not None:
                yield response.follow(nextpage, callback=self.parse)
            for collurls in collurl:
                yield scrapy.Request(collurls, callback=self.content)

    def content(self,response):
        item = BiggirlItem()
        item['name'] = response.xpath("//div[@class='content']/h5/text()").extract()
        item['imgurl'] = response.xpath("//div[@class='content-pic']/a/img/@src").extract()
        yield item

        nextpage = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.content)

