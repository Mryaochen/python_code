# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JavproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    id = scrapy.Field()
    title = scrapy.Field()
    new_id = scrapy.Field()
    desc = scrapy.Field()
# class DetailItem(scrapy.Item):
#     new_id = scrapy.Field()
#     desc = scrapy.Field()