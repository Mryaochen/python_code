#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 11:32
# @Author  : name
# @Site    : 
# @File    : 08：线程池基本使用.py
# @Software: PyCharm
import time
#使用单线程串行方式执行

# def get_page(str):
#     print("正在下载：",str)
#     time.sleep(2)
#     print("下载成功：",str)
# name_list = ['xiaozi','aa','bb','cc']
# start_time = time.time()
# for i in range(len(name_list)):
#     get_page(name_list[i])
# end_time = time.time()
# print('%d second'%(end_time-start_time))

#使用线程池模块对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功：",str)
name_list = ['xiaozi','aa','bb','cc']
#实例化一个线程池对象
pool = Pool(4) #4个线程
#将列表中每一个列表元素传递给get_page方法进行处理
pool.map(get_page,name_list)

end_time = time.time()
print(end_time-start_time)