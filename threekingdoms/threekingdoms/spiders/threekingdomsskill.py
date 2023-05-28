import scrapy


class ThreekingdomsskillSpider(scrapy.Spider):
    name = "threekingdomsskill"
    # allowed_domains = ["gl.sanguosha.com"]
    start_urls = ["http://gl.sanguosha.com/more?type=1"]

    def parse(self, response):
        #解析三国杀武将名字+图片地址
        # pass
        li_list = response.xpath('//div[@class = "heros"]/ul/li')
        for li in li_list:
            #xpath 返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            heroName = li.xpath('./a/text()')[0].extract()
            heroImgpath = li.xpath('./a/img/@src').extract()

            print(heroName,heroImgpath)