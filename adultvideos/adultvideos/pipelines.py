# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline,FilesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import re



class AzImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['url']:
            yield Request(image_url,meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item'][0]
        name = re.sub(r'[？\\*|“<>:/()]','',name)

        image_guid = request.url.split('/')[-1]
        filename = u'/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item

class AzFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        #print(item['url'],'__'*100)
        #for file_url in item['url']:
        yield Request(item['url'],meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item'][0]
        name = re.sub(r'[？\\*|“<>:/()]','',name)

        image_guid = request.url.split('/')[-1]
        filename = u'/{0}/{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        files_path = [x['path'] for ok, x in results if ok]
        if not files_path:
            raise DropItem('Item contains no files')
        #item['image_paths'] = image_path
        return item