# -*- coding: utf-8 -*-
import scrapy
from adultvideos.items import AdultvideosItem
from scrapy_splash.request import SplashRequest, SplashFormRequest
import re

class AzSpider(scrapy.Spider):
    name = 'az'
    allowed_domains = ['110az.com']
    start_urls = [
#                  'http://110az.com/list/8.html',
#                  'http://110az.com/list/10.html',
#                  'http://110az.com/list/2.html',
#                  'http://110az.com/list/3.html',
                  'http://110az.com/list/4.html',
#                  'http://110az.com/list/1.html',
#                  'http://110az.com/list/5.html',
#                  'http://110az.com/list/9.html',
    ]

    def parse(self, response):
        urllist = response.xpath("//div[@class='pic']")
        for requrl in urllist:
            url = requrl.xpath(".//a/@href").extract()
            #print(url)

            nextpage  = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
            if nextpage is not None:
                yield response.follow(nextpage, callback=self.parse)
            for videourl in url:
                requrl = 'http://110az.com' + videourl
                yield SplashRequest(requrl, args={'wait': '5'},callback=self.content)

    def content(self,response):

        item = AdultvideosItem()
        item['name'] = response.xpath("//*[@id='w700']/div[1]/h1/text()[2]").extract()
        resp= response.xpath("//*[@id='w700']/div[1]/script[2]/text()").extract()
        pattern = re.compile(r'[a-zA-z]+://[^\s]*')
        allurl = re.findall(pattern, resp[0])
        videourl = allurl[0].replace("'","").replace(",","")
        #print(type(videourl))
        item['url'] = videourl
        yield item

