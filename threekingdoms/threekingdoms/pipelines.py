# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#导入数据库包
import pymysql

class ThreekingdomsPipeline:


    fp = None
    #重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫...')
        self.fp = open('./hero.txt','w',encoding='utf-8')

    # 专门用来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        heroName = item['heroName']
        heroImgpath = item['heroImgpath']

        self.fp.write(heroName+':'+heroImgpath+'\n')
        return item #就会传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()

#管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
#模仿 写一个类存储到mysql中
class mysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='threekingdoms',charset='utf-8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            #执行sql语句
            self.cursor.execute('insert into threekingdoms values("%s","%s")'%(item["heroName"],item["heroImgpath"]))
            self.conn.commit() #提交
        except Exception as e:
            print(e)
            self.conn.rollback() #回滚
        return item  # 就会传递给下一个即将被执行的管道类
    def close_spider(self,spider):
        self.cursor.close() #关闭游标
        self.conn.close() #关闭连接

#爬虫文件提交的item类型的对象最终会提交给哪一个管道类？
    #先执行的管道类
        #--- return item --- #就会传递给下一个即将被执行的管道类