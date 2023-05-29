# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreekingdomsItem(scrapy.Item): #在item类中定义相关的属性
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    heroName = scrapy.Field()
    heroImgpath = scrapy.Field()