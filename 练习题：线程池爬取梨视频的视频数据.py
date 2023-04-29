#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 11:54
# @Author  : name
# @Site    : 
# @File    : 练习题：线程池爬取梨视频的视频数据.py
# @Software: PyCharm

#需求：爬取梨视频的视频数据
import requests
from UA import headers
from lxml import etree
import re
#原则：线程池处理的是阻塞且耗时的操作

if __name__ == '__main__':
    import requests
    import os
    import random
    from lxml import etree
    from multiprocessing.dummy import Pool as ThreadPool

    # headers = {
    #     "User-Agent":
    #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
    # }
    headers = headers
    # 原则：线程池处理的是阻塞且耗时的操作
    # 对下述url发起请求，解析出视频详情页的url和视频名称
    # 请求页面数据
    # url = "https://www.pearvideo.com/category_59"
    url = 'https://www.pearvideo.com/panorama'
    response = requests.get(url=url, headers=headers)
    page_text = response.text

    # 对页面数据进行xpath解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//ul[@id='listvideoListUl']/li")
    videos = []  # 用来存储视频的标题和链接
    for li in li_list:
        # 分别解析出每个视频详情页的链接和视频的标题
        # 注意：视频链接不完整，需要拼接
        detail_url = "https://www.pearvideo.com/" + li.xpath("./div/a/@href")[0]
        # 获取的标题文本，后面加上视频格式后缀".mp4"
        detail_title = li.xpath("./div/a/div[2]/text()")[0] + '.mp4'

        # 对详情页的url发请求并获取响应数据
        detail_page_text = requests.get(url=detail_url, headers=headers).text

        # 得到的数据是动态加载的，这个一定要验证一下response
        #https://www.pearvideo.com/videoStatus.jsp?contId=1721471&mrd=0.4796601486810357
        # 去掉问号后面用&连接的两个参数
        ajax_url = "https://www.pearvideo.com/videoStatus.jsp?"
        # 从前面详情页数据中解析出的"video_1746440"中分离出1746440这一部分，作为params中的contId
        cont_Id = li.xpath("./div/a/@href")[0].split("_")[-1]
        # 封装好get请求的参数，"mrd"是一个介于0和1之间的随机数，用random模块下的random()方法，注意要转成字符串类型
        params = {"contId": cont_Id, "mrd": str(random.random())}
        # 请求头中要加上Referer，这个和params中的contId都是动态的，且需要拼接
        # 加了'Referer': 'https://www.pearvideo.com/video_1746440'后就不会显示该文章已下架了
        #Referer https://www.pearvideo.com/video_1721471
        # ajax_headers = {
        #     "User-Agent":
        #         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
        #     "Referer":
        #         "https://pearvideos.com/video_" + cont_Id
        # }
        ajax_headers = headers
        ajax_headers["Referer"] =  "https://pearvideos.com/video_" + cont_Id
        # 对ajax中的视频链接发起请求，并获取响应数据，注意响应数据的类型是json类型，返回的是一个字典！！
        ajax_data = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()

        # 可以查看抓包工具--network--XHR--response，发现返回的结果是三层字典，需要一层一层地把视频地址srcUrl给剥出来
        video_url = ajax_data["videoInfo"]['videos']["srcUrl"]
        # print(video_url)  用于验证是否能爬取到url，成功！！
        # 但解析出来的视频地址是一个加密后的伪地址，需要将中间的一串13位数字改成cont-cont_id，方可得到真地址
        # 伪地址：https://video.pearvideo.com/mp4/third/20211123/1638172217395-12719568-193109-hd.mp4
        # 真地址：https://video.pearvideo.com/mp4/third/20211123/cont-1746440-12719568-193109-hd.mp4
        # 下面开始替换字符（俺不会正则QAQ，一直匹配不了ORZ）

        # 先将伪地址用"/"切割为列表,['https:', '', 'video.pearvideo.com', 'mp4', 'third', '20211123', '1638180827144-12719568-193109-hd.mp4']
        list1 = video_url.split("/")
        # 取出列表中的最后一个字符串：'1638180827144-12719568-193109-hd.mp4',将其用"-"切割为列表
        # ['1638180827144', '12719568', '193109', 'hd.mp4']
        list2 = list1[-1].split("-")
        # 用"cont-1746440"替换掉列表中的第一个字符串：'1638180827144'
        list2[0] = "cont-" + cont_Id
        # 用-把list2中的元素连接成一个字符串再替换list1中的最后一个元素
        list1[-1] = "-".join(list2)
        # 再将list1中的元素连成一个字符串就搞定了
        video_url_valid = "/".join(list1)
        # print(video_url_valid)  测试无误！！！
        # 将视频标题和链接封装到字典中
        video_info = {"Name": detail_title, "Url": video_url_valid}
        # 将单个视频的信息的字典存储到列表中
        videos.append(video_info)
    # 如果文件夹不存在则创建文件夹，用来放视频
    if not os.path.exists("./pearvideos"):
        os.mkdir("./pearvideos")


    # 定义一个下载视频的函数
    def download_video(dic):
        # 提示进度
        print(f"{dic['Name']} 正在下载......")
        # 向视频链接发送请求
        u = dic["Url"]
        video_data = requests.get(url=u, headers=headers).content
        # 持久化存储
        # with open()是上下文管理器，不需要手动进行close()关闭操作，写入二进制数据的时候，要用wb模式打开
        with open(f"pearvideos/{dic['Name']}", "wb") as fp:
            fp.write(video_data)
            print(f"{dic['Name']} 下载成功！！！")


    # 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
    pool = ThreadPool(4)  # 声明一个Pool对象，子线程数为4
    pool.map(download_video, videos)  # 函数为download_videos, 将列表videos中的各字典元素作为函数的参数
    # 关闭子线程
    pool.close()
    # 关闭主线程
    pool.join()



    # #1
    # url = 'https://www.pearvideo.com/panorama'
    # #2
    # page_text = requests.get(url=url,headers=headers).text
    # #3
    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
    # for li in li_list:
    #     detail_url = 'https://www.pearvideo.com/' + li.xpath('.//a/@href')[0]
    #     name = li.xpath('.//a/div[2]/text()')[0] + '.mp4'
    #     print(detail_url,name)
    #     #对详情页的url发起请求
    #     detail_page_text = requests.get(url=detail_url,headers=headers).text
    #     #从详情页中解析出视频的地址（url）
    #     '''
    #         {
    #             "resultCode":"1",
    #             "resultMsg":"success", "reqId":"a9a31924-7328-4fe4-83d6-19481b50c962",
    #             "systemTime": "1682742125255",
    #             "videoInfo":{"playSta":"1","video_image":"https://image.pearvideo.com/cont/20210226/cont-1721471-12558390.png","videos":{"hdUrl":"","hdflvUrl":"","sdUrl":"","sdflvUrl":"","srcUrl":"https://video.pearvideo.com/mp4/adshort/20210226/1682742125255-15616726_adpkg-ad_hd.mp4"}}
    #         }
    #     '''
    #     ex = '"srcUrl":"(.*?)"}'
    #     video_url = re.findall(ex,detail_page_text,re.S)[0]
    #     print(video_url)

