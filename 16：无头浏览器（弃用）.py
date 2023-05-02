#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 15:54
# @Author  : name
# @Site    : 
# @File    : 16：无头浏览器（弃用）.py
# @Software: PyCharm
from selenium import webdriver
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
import time
#实现规避检测
from selenium.webdriver import ChromeOptions
#创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 86
Current browser version is 13.5.2042.0 with binary path D:\installation\360Chrome\Chrome\Application\360chrome.exe
'''
# chrome_options.binary_location = r"D:\installation\360Chrome\Chrome\Application\360chrome.exe"  # 这里是360安全浏览器的路径
# chrome_options.add_argument(r'--lang=zh-CN')  # 这里添加一些启动的参数
#驱动路径
path = r'./drivers/chromedriver.exe'

#创建浏览器对象
driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)

#上网
url = 'https://www.baidu.com'
driver.get(url)
time.sleep(3)
page_text = driver.page_source
print(page_text)
driver.save_screenshot('baidu.png')

driver.quit()