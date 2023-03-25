# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 01：requests爬取百度首页.py
# Time       ：2023/3/22 21:58
# Author     ：DarkPlanet
# version    ：python 3.8.8
# Description：
"""
import requests
if __name__ == '__main__':
    #1  指定url
    url = 'https://www.baidu.com/'
    #2  发起请求
    #get方法 会返回一个响应对象
    res = requests.get(url = url)
    #3 获取响应数据 .text返回的是字符串形式的响应数据
    page_text = res.text
    print(page_text)
    #4 持久化存储
    with open('./baidu.com.html','w',encoding='utf-8') as fg:
        fg.write(page_text)
    print('爬取完成。')