#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 21:05
# @Author  : name
# @Site    : 
# @File    : 05：爬取图片.py
# @Software: PyCharm
import requests
if __name__ == '__main__':
    #1 指定url
    url = 'https://s2.doyo.cn/img/63/bf/65a68c017b51118b456b.jpg'
    #2 发起请求
    #3 获取响应数据 -- content 返回的是二进制形式的图片数据
    # text(字符串) content (二进制) json()(对象类型)
    img_data = requests.get(url=url).content

    with open('./tuhu.jpg','wb') as fp:  # 'w'写入模式 'b'二进制
        fp.write(img_data)