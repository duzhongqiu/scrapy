# -*- coding: utf-8 -*-
import scrapy
from adultvideos.items import AdultvideosItem

class AzSpider(scrapy.Spider):
    name = 'azimg'
    allowed_domains = ['110az.com']
    start_urls = ['http://110az.com/html/part/16.html',
                  'http://110az.com/html/part/17.html',
                  'http://110az.com/html/part/18.html',
                  'http://110az.com/html/part/19.html',
                  'http://110az.com/html/part/20.html',
                  'http://110az.com/html/part/21.html',
                  'http://110az.com/html/part/22.html',
                  'http://110az.com/html/part/23.html',]

    def parse(self, response):
        urllist = response.xpath('//*[@id="ks_xp"]/div/div[2]')
        for requrl in urllist:
            url = requrl.xpath(".//table/tbody/tr/td[1]/a[2]/@href").extract()
            #print(url)
            nextpage = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
            if nextpage is not None:
                yield response.follow(nextpage, callback=self.parse)

            for videourl in url[3:]:
                requrl = 'http://110az.com' + videourl
                yield scrapy.Request(requrl, callback=self.content)

    def content(self,response):
        item = AdultvideosItem()
        item['name'] = response.xpath("//*[@id='ks_xp']/div/div[1]/text()").extract()
        item['url'] = response.xpath("//*[@id='ks_xp']/div/div[2]/div/div/img/@src").extract()
        yield item
