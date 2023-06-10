# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DianyingproPipeline:
    def process_item(self, item, spider):
        # dianying_name = item['dianying_name']
        # dianying_desc = item['dianying_desc']
        print(item)
        # print(dianying_name)
        return item
