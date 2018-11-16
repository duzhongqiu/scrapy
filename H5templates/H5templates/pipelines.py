# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import re


class h5templateimgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield Request(image_url,meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item'][0]
        name = re.sub(r'[？\\*|“<>:/()0123456789]','',name)

        image_guid = request.url.split('/')[-1]
        filename = u'/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        #item['image_paths'] = image_path
        return item

class h5templatefilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['downloadurl']:
            yield Request(file_url,meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item'][0]
        name = re.sub(r'[？\\*|“<>:/()0123456789]','',name)

        image_guid = request.url.split('/')[-1]
        filename = u'/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        files_path = [x['path'] for ok, x in results if ok]
        if not files_path:
            raise DropItem('Item contains no files')
        #item['image_paths'] = image_path
        return item