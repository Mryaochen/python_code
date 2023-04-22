#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 21:57
# @Author  : name
# @Site    : 
# @File    : 练习题：xpath爬取站长素材免费简历rar.py
# @Software: PyCharm

import requests
import os
from lxml import etree
from UA import headers

if __name__ == '__main__':
    if not os.path.exists('./简历模板'):
        os.mkdir('./简历模板')
    #1-921
    for one in range(1,5):
        if one == 1:
            url = 'https://sc.chinaz.com/jianli/free.html'
        else:
            url = f'https://sc.chinaz.com/jianli/free_{one}.html'
        print('当前爬取的url为>>>',url)
        # #1 指定url - 站长之家素材
        # url = 'https://sc.chinaz.com/jianli/free.html'
        #2 UA伪装
        headers = headers
        #3 发起请求获取响应数据
        page_text = requests.get(url = url , headers= headers).text
        #实例化etree
        tree = etree.HTML(page_text)
        #找到超链接href 列表
        href_list = tree.xpath('//div[@class = "sc_warp  mt20"]//div[@id = "container"]/div/p/a/@href')
        # print(href_list)
        #遍历新的url
        for new_url in href_list:
            #简历免费下载页url与页面响应数据
            new_page_text = requests.get(url=new_url, headers=headers).text
            new_tree = etree.HTML(new_page_text)
            #获取download_list列表
            download_list = new_tree.xpath('//div[@id = "down"]/div[2]/ul/li/a/@href')
            resume_name = new_tree.xpath('//div[@class = "ppt_tit clearfix"]/h1/text()')[0]
            resume_name = resume_name.encode('iso-8859-1').decode('utf-8')
            #对download_list第一个地址发起请求，获取二进制响应数据
            rar_data = requests.get(url = download_list[0],headers=headers).content
            filename = './简历模板/' + resume_name + '.rar'
            with open(filename,'wb') as fp:
                fp.write(rar_data)
            fp.close()
            print(filename,'爬取成功！')


