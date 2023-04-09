# -*- coding: utf-8 -*-
# @Time    : 2023/4/5 19:07
# @Author  : name
# @Site    : 
# @File    : 练习题：xpath实战-58二手房.py
# @Software: PyCharm

import requests
from lxml import etree
from UA import headers
if __name__ == '__main__':
    #1 指定url
    url = 'https://sh.58.com/ershoufang/?'
    # UA伪装
    headers = headers
    #2 发起请求获取响应数据
    # 获取整张数据
    page_text = requests.get(url=url, headers=headers).text
    # 将得到的数据树化
    tree = etree.HTML(page_text)
    # 获取整个数据
    div_list = tree.xpath('//section[@class="list"]/div')
    print(div_list)
    # 创建文件
    fp = open('./58fangyuan.txt', 'w', encoding='utf-8')
    # 获得数据中的标题
    for div in div_list:
        an = div.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        print(an)
        fp.write(an + '\n' + '.\n')
