#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:14
# @Author  : name
# @Site    : 
# @File    : 获取代理IP池.py
# @Software: PyCharm

import requests
import json
import random
class FreeIP():
    def __init__(self):
        self.url = "http://proxylist.fatezero.org/proxy.list"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    def check_ip(self, ip_list):
        correct_ip = []
        for ip in ip_list:
            if len(correct_ip) > 10: # 可以根据自己的需求进行更改或者注释掉
                break
            ip_port = "{}:{}".format(ip["host"],ip["port"])
            proxies = {'https': ip_port}
            try:
                response = requests.get('https://icanhazip.com/', proxies=proxies,
                                        timeout=3).text  # 如果请求该网址，返回的IP地址与代理IP一致，则认为代理成功
                                                        # 可以更改timeout时间
                if response.strip() == ip["host"]:
                    print("可用的IP地址为：{}".format(ip_port))
                    correct_ip.append(ip_port)
            except:
                print("不可用的IP地址为：{}".format(ip_port))
        return correct_ip


    def run(self):
        response =  requests.get(url=self.url).content.decode()

        ip_list = []
        proxies_list = response.split('\n')

        for proxy_str in proxies_list:
            try:
                proxy = {}
                proxy_json = json.loads(proxy_str)
                if proxy_json["anonymity"] == "high_anonymous" and proxy_json["type"] == "https":
                    host = proxy_json['host']
                    port = proxy_json['port']
                    proxy["host"] = host
                    proxy["port"] = port
                    ip_list.append(proxy)
                    print("{}符合https和高匿条件".format(host))
            except:
                print(proxy_str)

        correct_ip = self.check_ip(ip_list)
        print("可用的IP地址有{}个".format(len(correct_ip)))
        print(correct_ip)
        return correct_ip

if __name__ == '__main__':
    ip = FreeIP()
    correct_ip = ip.run()
    for ip in correct_ip:
        with open('ip.txt','a+',encoding='utf-8') as fp:
            fp.write(ip + '\n')
        fp.close()
