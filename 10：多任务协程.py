#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 18:20
# @Author  : name
# @Site    : 
# @File    : 10：多任务协程.py
# @Software: PyCharm
import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    #当在asyncio中遇到阻塞操作必须手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)
start = time.time()
urls = [
    'www.baidu.com',
    'www.qq.com',
    'www.sougou.com'
]
#任务列表：存放多个任务对象
tasks = []
for url in urls:
    coro = request(url)
    task = asyncio.ensure_future(coro)
    tasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中 asyncio.wait()固定写法
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print(end-start)