# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class BoleSpiderPipeline(object):
    def __init__(self):
        self.fp = open('bole.xls','w',newline='',encoding='utf-8')
        self.DATA = []
        self.header = {
            'title','author','content'
        }
        self.writer = csv.DictWriter(self.fp,self.header)
        self.writer.writeheader()
    def process_item(self, item, spider):
        self.DATA.append(item)
        self.writer.writerows(self.DATA)
        return item
    def close_spider(self,spider):
        self.fp.close()