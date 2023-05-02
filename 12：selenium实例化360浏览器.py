#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 10:58
# @Author  : name
# @Site    : 
# @File    : 12：selenium实例化360浏览器.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, warnings

# 关闭警告显示
warnings.filterwarnings("ignore")

# 启动360安全浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"D:\installation\360Chrome\Chrome\Application\360chrome.exe"  # 这里是360安全浏览器的路径
chrome_options.add_argument(r'--lang=zh-CN')  # 这里添加一些启动的参数
# driver = webdriver.Chrome(chrome_options=chrome_options) #驱动已放在D:\develop\Python38路径下，此路径默认在path中
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='./drivers/chromedriver.exe') #executable_path指定驱动路径)
driver.get('https://www.baidu.com/')  # 启动浏览器，打开对应网页
time.sleep(4)  # 等待浏览器启动
# kw = driver.find_element_by_id('kw')  # 寻找搜索框 仅限老版本
kw = driver.find_element(By.ID,'kw')
kw.send_keys('Python selenium 控制 360安全浏览器')  # 向搜索框键入文字
time.sleep(1)
kw.send_keys(Keys.ENTER)  # 按回车键搜索
page_text = driver.page_source #获取页面源码数据
print(page_text)
time.sleep(20)
driver.close()
