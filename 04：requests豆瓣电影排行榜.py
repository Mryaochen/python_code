# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 04：requests豆瓣电影排行榜.py
# Time       ：2023/3/25 17:15
# Author     ：DarkPlanet
# version    ：python 3.8.8
# Description：
"""
import requests
import json
if __name__ == '__main__':
    #1. 指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    #2. UA为欸装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    #3。get参数
    param = {
        'type': '5',
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }
    #4. 发起请求
    res = requests.get(url=url,params=param,headers=headers)
    #5. 获取响应数据 Content-Type: application/json 已知返回json格式，可以用.json()返回对象
    list_obj = res.json()
    #6. 持久化存储
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_obj,fp = fp,ensure_ascii=False)#ensure_ascii 中文不适用ascii
    print('douban toplist 爬取成功')