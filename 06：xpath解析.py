#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/5 14:53
# @Author  : name
# @Site    : 
# @File    : 06：xpath解析.py
# @Software: PyCharm

from lxml import etree
if __name__ == '__main__':
    #实例化一个etree对象，茄酱被解析的源码加载到该对象中
    # tree = etree.parse('qq.html')
    # r = tree.xpath('/html/head/title')
    # print(r)
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('qq.html', parser=parser)
    # result = etree.tostring(html, encoding='utf-8').decode('utf-8')
    # print(result)
    tree = etree.parse('qq.html', parser=parser)
    # r = tree.xpath('//div[@class="layout qq-top cf"]')
    r = tree.xpath('//title/text()')

    print(r)

