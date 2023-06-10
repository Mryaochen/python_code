import scrapy
from dianyingPro.items import DianyingproItem

class DianyingSpider(scrapy.Spider):
    name = "dianying"
    # allowed_domains = ["dianyi.ng"]
    start_urls = ["https://dianyi.ng/v/action.html "]
    # start_urls = ["https://www.hacg.sbs/wp/anime.html"]
    url = 'https://dianyi.ng/v/action-%d.html'
    # url = 'https://www.hacg.sbs/wp/anime.html/page/%d'
    page_num = 2
    def detail_parse(self, response):
        item = response.meta['item']
        dianying_desc =response.xpath('//*[@id="main"]/div/div[1]/div[3]/div[2]/div[8]/div/span/text()').extract_first()
        # dianying_desc = response.xpath('//*[@id="content"]/article/div[1]//text()').extract()
        # dianying_desc = ''.join(dianying_desc) #空格拼接
        item['dianying_desc'] = dianying_desc
        # print(dianying_desc)
        # print(item)
        yield item
    def parse(self, response):
        # pass
        # item = DianyingproItem() -------------->放在循环外面 导致只抓取列表最后一条
        # h1_list = response.xpath('//*[@id="content"]/article//h1')
        div_list = response.xpath('//*[@id="main"]/div[1]/div[2]/div[2]/div/div/div[2]')
        # print(h1_list)
        # for h in h1_list:
        for div in div_list:
            item = DianyingproItem()
            # dianying_name = h.xpath('./a/text()').extract_first()
            dianying_name = div.xpath('./a/text()').extract_first()
            # print(dianying_name)
            item['dianying_name'] = dianying_name
            dianying_url ='https://dianyi.ng/' + div.xpath('.//a/@href').extract_first()
            # dianying_url =  h.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=dianying_url,callback=self.detail_parse,meta={'item':item})
        if self.page_num <= 3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)