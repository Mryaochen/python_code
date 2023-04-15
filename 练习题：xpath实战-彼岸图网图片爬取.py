#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/9 18:18
# @Author  : name
# @Site    : 
# @File    : 练习题：xpath实战-彼岸图网图片爬取.py
# @Software: PyCharm

import requests
from lxml import etree
from UA import headers
import os
if __name__ == '__main__':
    #时灵时不灵
    url = 'https://pic.netbian.com/e/search/result/?searchid=4318'

    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    print(li_list)
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
        new_response = requests.get(url=img_src, headers=headers).text
        new_tree = etree.HTML(new_response)
        # 数据解析：src的属性值  alt属性
        download = 'https://pic.netbian.com' + new_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        img_name = new_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0] + '.png'
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        # 请求图片进行持久化存储
        img_data = requests.get(url=download, headers=headers).content
        img_path = 'picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')


