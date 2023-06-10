import scrapy


class BossSpider(scrapy.Spider):
    name = "boss"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python%E7%88%AC%E8%99%AB&city=101020100"]

    def parse(self, response):
        # pass
        response.xpath('')
