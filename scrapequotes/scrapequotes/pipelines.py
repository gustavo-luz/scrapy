# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapequotesPipeline(object):
    def process_item(self, item, spider):
        print("pipeline :"+item['title'][0]+item['author'][0])
        return item
