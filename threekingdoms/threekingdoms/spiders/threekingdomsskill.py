import scrapy
import pprint
from threekingdoms.items import ThreekingdomsItem
class ThreekingdomsskillSpider(scrapy.Spider):
    name = "threekingdomsskill"
    # allowed_domains = ["gl.sanguosha.com"]
    start_urls = ["http://gl.sanguosha.com/more?type=1"]
    # 基于终端指令 持久化存储
    # def parse(self, response):
    #     #解析三国杀武将名字+图片地址
    #     # pass
    #     li_list = response.xpath('//div[@class = "heros"]/ul/li')
    #     all_data = []
    #     for li in li_list:
    #         #xpath 返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract可以将Selector对象中data参数存储的字符串提取出来
    #         heroName = li.xpath('./a/text()')[0].extract()
    #         heroImgpath = li.xpath('./a/img/@src').extract()
    #         hero = {
    #             'heroName':heroName,
    #             'heroImgpath':heroImgpath
    #         }
    #         all_data.append(hero)
    #     return all_data   #基于终端指令
    #     #     print(heroName,heroImgpath)
    #     # pprint.pprint(all_data)

    # 基于管道 持久化存储
    def parse(self, response):
        #解析三国杀武将名字+图片地址
        # pass
        li_list = response.xpath('//div[@class = "heros"]/ul/li')

        for li in li_list:
            #xpath 返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            heroName = li.xpath('./a/text()')[0].extract()
            heroImgpath = li.xpath('./a/img/@src').extract()[0]

            item = ThreekingdomsItem()
            item['heroName'] = heroName
            item['heroImgpath'] = heroImgpath

            yield item #将item提交给管道