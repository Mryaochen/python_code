#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 16:15
# @Author  : name
# @Site    : 
# @File    : 16：Edge无头浏览器.py
# @Software: PyCharm
from selenium import webdriver
#导入浏览器设置相关的类 实现无头
from selenium.webdriver.edge.options import Options
import time

#无头/无可视化界面设置
edge_options = Options()
#使用无头模式
edge_options.add_argument('--headless')
#禁用GPU，防止无头模式出现莫名BUG
edge_options.add_argument('--disable-gpu')
#参数传入浏览器
driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe',options=edge_options)  #executable_path指定驱动路径
# driver.maximize_window() #最大化窗口
driver.get('https:www.baidu.com')
time.sleep(5)
page_text = driver.page_source #获取页面源码数据
print(page_text)
driver.save_screenshot('baidu.png')
driver.quit()