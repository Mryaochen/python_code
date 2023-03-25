# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 02：requests简易网页爬取器.py
# Time       ：2023/3/23 21:25
# Author     ：DarkPlanet
# version    ：python 3.8.8
# Description：
"""
import requests
if __name__ == '__main__':
    #step 1 :指定url
    # url = 'https://www.baidu.com/s'
    url = 'https://www.sogou.com/web?'
    #封装 params 与 header
    kw = input('输入一个关键词:')
    # param = {
    #     'wd':kw
    # }
    param = {
        'query':kw
    }
    #UA伪装，封装User-Agent
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    #step 2 发起请求
    res = requests.get(url=url,params=param,headers=headers)
    #step 3 获取响应数据
    page_text = res.text
    #step 4 持久化存储
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'爬取成功。')