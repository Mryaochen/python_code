# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JavproPipeline:
    def process_item(self, item, spider):
        #如何判断item的类型
        # if item.__class__.__name__ == 'DetailItem':
        #     print(item['new_id'],item['desc'])
        # else:
        #     print(item['id'],item['title'])
        print(item)
        return item
