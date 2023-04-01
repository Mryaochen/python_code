#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/1 10:26
# @Author  : name
# @Site    : 
# @File    : 练习题：爬取QQ新闻网图片.py
# @Software: PyCharm
import requests
import re
import os
from UA import headers
if __name__ == '__main__':
    #创建文件夹
    if not os.path.exists('./qq图片'):
        os.mkdir('./qq图片')
    #1 指定url
    url = 'https://www.qq.com/'
    # UA伪装
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    # }
    headers = headers
    # 使用通用爬虫 对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text

    #使用聚焦爬虫将页面中所有的图片进行解析/提取
    ex = '<div class="pic fl">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    print(img_src_list)
    for src in img_src_list:
        #补全图片地址
        if 'https:' not in src:
            src = 'https:' + src
        #补全图片名称
        img_name = src.split('/')[-2]
        img_path = './qq图片/' + img_name + '.jpg'
        img_data = requests.get(url=src,headers=headers).content
        with open(img_path,'wb') as fp:
            fp.write(img_data)
        fp.close()
        print(img_name,'保存成功')
    with open('qq.com.html','w',encoding='utf-8') as fp:
        fp.write(page_text)

    fp.close()
    print( 'qq保存成功')