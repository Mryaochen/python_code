import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]

    def parse(self, response):
        # pass
        div_list = response.xpath('//div[@class="container"][2]/div[2]/div')
        for div in div_list: #注意伪属性
            src ='https:' +  div.xpath('./img/@data-original').extract_first()
            img_desc =div.xpath('./img/@alt').extract_first()
            # print(src)

            item = ImgsproItem()
            item['src'] = src

            yield item