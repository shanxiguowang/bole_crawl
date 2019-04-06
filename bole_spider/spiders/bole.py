# -*- coding: utf-8 -*-
import scrapy
from bole_spider.items import BoleSpiderItem
from scrapy_redis.spiders import RedisSpider




class BoleSpider(RedisSpider):
    name = 'bole'
    allowed_domains = ['importnew.com']
    # start_urls = ['http://www.importnew.com/all-posts']
    redis_key = 'bole:start_urls'

    def parse(self, response):
     urls = response.xpath("//div[@class='grid-8']//div[@class='post-meta']//a[@class='meta-title']/@href").getall()
     for url in urls:
        yield scrapy.Request(url=url,callback=self.paesr_details)

     next_url = response.xpath("//div[contains(@class,'navigation')]/a[contains(@class,'next')]/@href").get()
     if next_url:
        yield  scrapy.Request(url=next_url,callback=self.parse)

    def paesr_details(self,response):
        title = response.xpath("//div[@class='entry-header']/h1/text()").get()
        author = response.xpath("//div[@class='copyright-area']/a/text()").get()
        content = response.xpath("//div[@class='entry']").get()
        item = BoleSpiderItem(title=title,author=author,content=content)
        return item