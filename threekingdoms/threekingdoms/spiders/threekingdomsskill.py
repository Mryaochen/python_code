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
    # def parse(self, response):
    #     #解析三国杀武将名字+图片地址
    #     # pass
    #     li_list = response.xpath('//div[@class = "heros"]/ul/li')
    #
    #     for li in li_list:
    #         #xpath 返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract可以将Selector对象中data参数存储的字符串提取出来
    #         heroName = li.xpath('./a/text()')[0].extract()
    #         heroImgpath = li.xpath('./a/img/@src').extract()[0]
    #
    #         item = ThreekingdomsItem()
    #         item['heroName'] = heroName
    #         item['heroImgpath'] = heroImgpath
    #
    #         yield item #将item提交给管道



    #基于spider爬取全站
    #生成一个通用的url模板（不可变）
    url = 'http://gl.sanguosha.com/more?type=4&page=%d'
    page_num = 1
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

        if self.page_num <= 3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            #手动请求发送：callback回调函数是专门给用作于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)