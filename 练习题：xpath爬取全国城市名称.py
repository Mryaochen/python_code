#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 11:23
# @Author  : name
# @Site    : 
# @File    : 练习题：xpath爬取全国城市名称.py
# @Software: PyCharm

import requests
from lxml import etree
from UA import headers
from requests.packages import  urllib3 #这里是由于这个网页的证书没有被官方CA机构信任，所以这里会出现证书验证的错误。
if __name__ == '__main__':
    #指定URL
    url = 'https://www.aqistudy.cn/historydata/'
    #UA伪装
    headers = headers
    #发起请求获取请求数据 .text
    urllib3.disable_warnings() #下面代码调用了urllib3.disable_warnings()函数，来确保不会发生警告。
    page_text = requests.get(url=url,headers=headers,verify=False).text
    #实例化etree
    tree = etree.HTML(page_text)
    #找到城市li标签
    li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    city_name_list = []
    for li in li_list:
        city_name = li.xpath('./a/text()')[0]
        city_name_list.append(city_name)
    city_name_list = list(set(city_name_list)) #将列表转化为集合再转化为列表，利用集合的自动去重功能。简单快速。缺点是：使用set方法无法保证去重后的顺序。
    print(len(city_name_list))
    print(city_name_list)