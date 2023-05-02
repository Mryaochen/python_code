#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 12:05
# @Author  : name
# @Site    : 
# @File    : 15：selenium对iframe的处理.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#导入动作链对应的类
from selenium.webdriver import ActionChains
driver = webdriver.Edge(executable_path='./drivers/msedgedriver.exe')  #executable_path指定驱动路径
# driver.maximize_window() #最大化窗口
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在于iframe标签之中，需要switch_to
driver.switch_to.frame('iframeResult') #切换浏览器标签定位的作用域
div = driver.find_element(By.ID,'draggable')
print(div)
#动作链
action = ActionChains(driver)
action.click_and_hold(div)#点击长按指定的标签

for i in range(5):
    #perform()立即执行动作链操作,move_by_offset(x,y)移动多少x,y像素
    action.move_by_offset(40,0).perform()
    time.sleep(0.3)
#释放动作链
action.release()
time.sleep(5)
# page_text = driver.page_source #获取页面源码数据
# print(page_text)
driver.quit()
