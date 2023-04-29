#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 16:35
# @Author  : name
# @Site    : 
# @File    : 09：协程asyncio.py
# @Software: PyCharm

import asyncio

# async def main(): #coroutine function
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
# coro = main() #coroutine object
# asyncio.run(coro)

async def request(url):
    print('正在请求的url是',url)
    print('请求成功',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
coro = request('www.baidu.com')

# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(coro)
#
# #task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建一个task对象
# task = loop.create_task(coro)
# print(task)
#
# loop.run_until_complete(task)
# print(task)
#
# #future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coro)
# print(task)
# loop.run_until_complete(task)
# print(task)
def callback_func(task):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coro)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)