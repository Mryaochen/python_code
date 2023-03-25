# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 03：requests百度翻译英译中.py
# Time       ：2023/3/25 16:17
# Author     ：DarkPlanet
# version    ：python 3.8.8
# Description：
"""
import requests
import json
if __name__ == '__main__':
    #1、 指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    #2. UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    #3. post参数
    word = input('enter a word:')
    data = {
        'kw': word
    }
    #4. 发起请求
    res = requests.post(url=post_url,data=data,headers=headers)
    #5. 获取响应数据 Content-Type: application/json 已知返回json格式，可以用.json()返回对象
    dic_obj = res.json()
    # print(dic_obj)
    #6. 持久化存储
    filename = word + '.json'
    # fp = open('./%s.json'%word,'w',encoding='utf-8')
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False) #ensure_ascii 中文不适用ascii
    fp.close() #暂不确定是否必要
    print('%s百度翻译结果爬取成功！'%word)