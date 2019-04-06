# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse

class BoleSpiderSpiderMiddleware(object):
   def __init__(self):
       self.driver = webdriver.Chrome(executable_path=r'D:\selenium\chromedriver_win32 (1)\chromedriver.exe ')
   def process_request(self,spider,request):
        self.driver.get(request.url)
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url,body=source,
                                request=request,encoding='utf-8')
        return response