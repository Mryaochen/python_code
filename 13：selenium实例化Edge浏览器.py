#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 11:07
# @Author  : name
# @Site    : 
# @File    : 13：selenium实例化Edge浏览器.py
# @Software: PyCharm
from selenium import webdriver
import time

# driver = webdriver.Edge() #实例化 调用Edge浏览器 #驱动已放在D:\develop\Python38路径下，此路径默认在path中
driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe')  #executable_path指定驱动路径
driver.maximize_window() #最大化窗口
driver.get('https:www.baidu.com')
time.sleep(5)
page_text = driver.page_source #获取页面源码数据
print(page_text)
driver.quit()