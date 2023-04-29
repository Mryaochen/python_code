#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 18:29
# @Author  : name
# @Site    : 
# @File    : 11：aiohttp实现多任务异步协程.py
# @Software: PyCharm
import requests
import asyncio
import time
import aiohttp
#使用aiohttp模块中的ClientSession
#搭配flask服务学习
start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]

async def get_page(url):
    print('正在下载',url)
    #requests发起的请求是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp：基于异步网络请求的模块
    # response = requests.get(url=url)
    async with aiohttp.ClientSession() as session:
        #get()、post()
        #UA伪装 headers,参数 params/data,代理IP,proxy='http://ip:port'(字符串不是字典)
        async with await session.get(url) as response:
            #page_text = response.text() #RuntimeWarning: coroutine 'ClientResponse.text' was never awaited
            #获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            #aiohttp与requests的区别
            #text()返回字符串形式的响应数据
            #read()返回二进制形式的响应数据
            #json()返回的就是json对象
    print('下载完毕',page_text)

tasks = []

for url in urls:
    coro = get_page(url)
    task = asyncio.ensure_future(coro)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print('总耗时',end-start)