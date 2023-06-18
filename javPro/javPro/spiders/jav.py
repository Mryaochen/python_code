import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.edge.options import Options
# from javPro.items import JavproItem,DetailItem
from javPro.items import JavproItem
class JavSpider(CrawlSpider):
    name = "jav"
    # allowed_domains = ["www.a66j.com"]
    start_urls = ["https://www.a66j.com/cn/vl_mostwanted.php"]

    rules = (
        Rule(LinkExtractor(allow=r"mode=&page=\d+"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow=r"./?v=\w+"), callback="parse_detail") #解析器阻塞
    )
    def __init__(self):
        super(JavSpider,self).__init__() #这里是关键 AttributeError: 'Spider' object has no attribute '_rules' 报错是init没有继承父类
        # 无头/无可视化界面设置
        self.edge_options = Options()
        # 使用无头模式
        self.edge_options.add_argument('--headless')
        # 禁用GPU，防止无头模式出现莫名BUG
        self.edge_options.add_argument('--disable-gpu')
        # 参数传入浏览器
        self.driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe',options=self.edge_options)  #executable_path指定驱动路径)
    #解析番号与标题
    def parse_item(self, response):
        # item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
        div_list = response.xpath('//*[@id="rightcolumn"]/div[2]/div/div')
        for div in div_list:
            id = div.xpath('./a/div[1]/text()').extract_first()
            title = div.xpath('./a/div[2]/text()').extract_first()
            # print(id,title)
            item = JavproItem()
            item['id'] = id
            item['title'] = title
            url = div.xpath('./a/@href').extract_first()
            new_url = 'https://www.a66j.com/cn' + url.split('.')[-1]
            # print(url,new_url)
            # yield item
            yield scrapy.Request(url=new_url, callback=self.parse_detail, meta={'item': item})
        # print(response)
    def parse_detail(self, response):
        new_id = response.xpath('//*[@id="video_id"]/table//tr/td[2]/text()').extract_first() #xpath表达式中出现“tbody”标签需要删除，否则异常
        desc = response.xpath('//*[@id="video_genres"]/table//tr/td[2]//text()').extract()
        desc = ''.join(desc)
        item = response.meta['item']
        # item = DetailItem()
        item['new_id'] = new_id
        item['desc'] = desc

        yield item
        # print(new_id,desc)
    def closed(self,spider):
        self.driver.quit()