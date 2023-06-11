import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
from selenium.webdriver.edge.options import Options
class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]
    models_urls = [] #存储板块对应的详情页的url
    #实例化一个浏览器对象
    def __init__(self):
        # 无头/无可视化界面设置
        self.edge_options = Options()
        # 使用无头模式
        self.edge_options.add_argument('--headless')
        # 禁用GPU，防止无头模式出现莫名BUG
        self.edge_options.add_argument('--disable-gpu')
        # 参数传入浏览器
        self.driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe',options=self.edge_options)  #executable_path指定驱动路径)
    #解析板块对应的详情页的URL
    def parse(self, response):
        # pass
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [1,2,4,5]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        #依次对每一个板块对应的页面发请求
        for url in self.models_urls:
            yield scrapy.Request(url,callback=self.parse_model)

    def parse_model(self,response):#解析每一个版块页面中对应的新闻标题和详情页的url
        div_list = response.xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyiproItem()
            item['title'] = title
            #对新闻详情页的url发请求
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):#专门解析新闻内容
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] =content
        yield item
    def closed(self,spider):
        self.driver.quit()