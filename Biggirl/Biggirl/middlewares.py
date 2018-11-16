# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BiggirlSpiderMiddleware(object):

    def process_request(self, request, spider):
        referer = request.url
        if referer:
            request.headers['referer'] = 'http://www.cssmoban.com/'

