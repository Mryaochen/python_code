#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 16:22
# @Author  : name
# @Site    : 
# @File    : 17：Edge浏览器规避selenium检测.py
# @Software: PyCharm
from selenium import webdriver
# 在这里导入浏览器设置相关的类
from selenium.webdriver.edge.options import Options
import time
# 反检测设置 #

edge_options = Options()

# 开启开发者模式
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 禁用启用Blink运行时的功能
edge_options.add_argument('--disable-blink-features=AutomationControlled')

# 将参数传给浏览器
driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe',options=edge_options)

# 启动浏览器
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
driver.get(url)
time.sleep(5)
driver.save_screenshot('检测.png')
driver.quit()