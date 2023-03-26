# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 练习题：requests爬取肯德基餐厅地址.py
# Time       ：2023/3/26 17:56
# Author     ：DarkPlanet
# version    ：python 3.8.8
# Description：
"""
import requests
import json
if __name__ == '__main__':
    #1、 指定url
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    #2、UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    #3、post参数
    cname = input('enter a city name in Chinese:')
    data = {
        'cname': cname,
        'pid':'',
        'pageIndex': '1',
        'pageSize': '10'
    }
    #4、 发起请求
    res = requests.post(url=post_url,data=data,headers=headers)
    #5、 获取响应数据 text
    # res_text = res.text
    dic_obj = res.json()
    # print(type(dic_obj))
    # print(res_text)
    #6、 持久化存储
    filename = cname + '肯德基餐厅地址.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print(cname,'肯德基餐厅地址爬取成功！')