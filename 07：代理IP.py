#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:01
# @Author  : name
# @Site    : 
# @File    : 07：代理IP.py
# @Software: PyCharm

from UA import headers
import requests
if __name__ == '__main__':
    #1 指定url
    url = 'https://www.baidu.com/s?wd=IP'
    #2 封装代理
    proxy = {
        'https':'20.111.54.16:8123'
    }
    #3 发起请求获取响应数据
    page_text = requests.get(url=url,headers=headers,proxies=proxy).text

    with open('./ip.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    fp.close()
    print('IP测试成功')