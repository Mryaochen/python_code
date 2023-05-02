#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 11:32
# @Author  : name
# @Site    : 
# @File    : 14：selenium实例化Firefox浏览器.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'D:\installation\Mozilla Firefox\firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary) #驱动已放在D:\develop\Python38路径下，此路径默认在path中
driver = webdriver.Firefox(firefox_binary=binary,executable_path='./drivers/geckodriver.exe') #executable_path指定驱动路径
# driver = webdriver.Firefox()
driver.maximize_window() #最大化窗口
driver.get('https:www.baidu.com')
time.sleep(5)
page_text = driver.page_source #获取页面源码数据
print(page_text)
driver.quit()