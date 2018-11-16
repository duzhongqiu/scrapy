# -*- coding: utf-8 -*-
import scrapy
from H5templates.items import H5TemplatesItem

class H5templateSpider(scrapy.Spider):
    name = 'h5template'
    allowed_domains = ['www.cssmoban.com']
    start_urls = ['http://www.cssmoban.com/cssthemes/']

    def parse(self, response):
        urllist = response.xpath("//ul[@class='thumbItem large clearfix']/li")
        for urlreq in urllist:
            url = urlreq.xpath(".//p/a/@href").extract()

            nextpage = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()  # 下一页url
            if nextpage is not None:
                yield response.follow(nextpage, callback=self.parse)
            for collurls in url:
                requrl = 'http://www.cssmoban.com' + collurls
                yield scrapy.Request(requrl, callback=self.content)

    def content(self,response):
        item = H5TemplatesItem()
        item['name'] = response.xpath("//div[@class='con-right']/h1/text()").extract()
        item['imgurl'] = response.xpath("//div[@class='large-Imgs']/img/@src").extract()
        item['downloadurl'] = response.xpath("//a[@class='button btn-down']/@href").extract()
        yield item


