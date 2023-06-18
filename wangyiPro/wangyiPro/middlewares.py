# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapy.http import HtmlResponse

from time import sleep
class WangyiproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):#spider爬虫对象
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        driver = spider.driver #获取在爬虫类中定义的浏览器对象
        if request.url in spider.models_urls:
            #response #板块对应的响应对象
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来不包含动态数据的响应对象
            driver.get(request.url) #对板块url发请求
            sleep(2)
            page_text = driver.page_source #包含了动态加载的数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)

            return new_response
        else:
            # response #其他请求对应的响应对象
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass


