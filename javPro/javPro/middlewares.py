# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy.http import HtmlResponse
from time import sleep
from scrapy import signals
from selenium.webdriver.common.by import By
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter



class JavproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    #封装UA池 - 尽可能多的将scrapy工程中的请求伪装成不同类型的浏览器身份
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    # 可被选用的代理IP - 尽可能多的将scrapy工程中的请求的IP设置成不同的,防止被反扒策略封禁本机IP
    PROXY_http = [
        '47.90.126.138:9090',
        '61.145.212.31:3128',
        '122.136.212.132:53281'
    ]
    PROXY_https = [
        '110.45.156.46:3128',
        '177.93.45.154:999',
        '39.106.60.216:3128'
    ]

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

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # 挑选出指定的响应对象进行篡改
        # 通过url指定request
        # 通过request指定response
        driver = spider.driver  # 获取在爬虫类中定义的浏览器对象
        if request.url == 'https://www.a66j.com/cn/vl_mostwanted.php' or 'https://www.a66j.com/cn/' in request.url:
            # response #板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来不包含动态数据的响应对象
            driver.get(request.url)  # 对板块url发请求
            sleep(1)
            try:
                ageButton = driver.find_element(By.XPATH, '//*[@id="adultwarningprompt"]/p/input[1]')
                ageButton.click()
                sleep(2)
            except Exception as e:
                print(e)
            page_text = driver.page_source  # 包含了动态加载的数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)

            return new_response
        else:
            # response  # 其他请求对应的响应对象
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        if request.url.split(':')[0] == 'http':

            # 代理
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:

            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)

        return request  # 将修正之后的请求对象进行重新请求发送

