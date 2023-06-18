import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest?id=1"]

    rules = (
        #规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        #LinkExtractor 链接提取器 根据指定规则（allow=“正则”）进行指定链接的提取
        # follow = True 可以将链接提取器 继续作用到 链接提取器提取到的链接 所对应的页面
        Rule(LinkExtractor(allow=r"id=1&page=\d+"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
        print(response)