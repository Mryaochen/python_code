#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/2 9:03
# @Author  : name
# @Site    : 
# @File    : 练习题：bs4爬取三国演义小说章节标题与内容.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from UA import headers
import os
if __name__ == '__main__':
    #创建文件夹
    if not os.path.exists('./三国演义'):
        os.mkdir('./三国演义')
    #1 指定URL
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    #2 UA伪装
    headers = headers
    #3 发起请求获取请求数据
    # page_text = requests.get(url=url,headers=headers).text 使用text解析乱码
    page_content = requests.get(url=url, headers=headers).content
    #4 实例化BeautifulSoup对象
    soup = BeautifulSoup(page_content, 'lxml')

    li_list = soup.select('.book-mulu li')
    # print(li_list)
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        #对详情页发请求获取响应数据解析章节内容
        # detail_page_text = requests.get(url=detail_url,headers=headers).text 使用text解析乱码
        detail_page_content = requests.get(url=detail_url, headers=headers).content
        #解析出详情页中相关的章节内容所在标签
        detail_soup = BeautifulSoup(detail_page_content,'lxml')
        div_tag = detail_soup.find('div',class_ = 'chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        filename = './三国演义/' + title + '.txt'
        with open(filename,'w',encoding='utf-8') as fp:
            fp.write(content)
        fp.close()
        print(title,'爬取成功！')