# python_code
# .gitignore
# python requirements.txt使用
pip freeze > requirements.txt # 生成requirements.txt

pip install -r requirements.txt # 从requirements.txt安装依赖

pip install -r requirements.txt -i https://pypi.douban.com/simple
当提示权限不够时，前面加上sudo

#通用式爬虫
    urllib 
    requests 重点
        1、指定url
            UA伪装 headers = {}
            post/get 参数 data/param = {}
        2、发起请求
        3、获取响应数据 response.status_code (响应码)
        4、持久化存储 json.dumps/with open() as fp
#聚焦爬虫 : 爬取页面中指定的页面内容
    数据解析 原理
        解析局部的文本内容，都会在标签之间或者标签对应的属性中提取
        1、进行指定标签的定位
        2、标签或者标签对应的属性中存储的数据值进行提取（解析）
    正则表达式
        <div class="pic fl">
            <a href="https://new.qq.com/rain/a/20230331A03B0500" target="_blank" data-beacon-expo="qn_elementid=yw9_1&amp;qn_event_type=show" data-beacon-click="qn_elementid=yw9_1&amp;qn_event_type=click" newsexpo="yw9_1" dt-imp-once="true" dt-eid="em_item_article" dt-params="article_url=https://new.qq.com/rain/a/20230331A03B0500&amp;article_type=&amp;dt_element_path=['em_item_article']">
            <img src="https://inews.gtimg.com/newsapp_bt/0/0331133600942_9768/0" alt="财政部：进一步完善税费优惠政策，支持小微企业、个体户">
            </a>
        </div>
        正则：ex = '<div class="pic fl">.*?<img src="(.*?)" alt.*?</div>'
    bs4
        1、实例化一个BeautifulSoup对象，并且将页面愿怕数据加载到该对象中
        2、通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
        -实例化BeautifulSoup对象
        from bs4 import BeautifulSoup
        -对象的实例化：
        1、将本地的html文档中的数据加载到该对象中
            fp = open('./qq.com.html','r',encoding='utf-8')
            soup = BeautifulSoup(fp,'lxml')
        2、将互联网上获取的页面源码加载到该对象中
            page_text = res.text
            soup = BeautifulSoup(page_text,'lxml')
        soup.tagName:返回第一次出现的tagName标签
        soup.find():属性定位
            - soup.find('tagName')相当于soup.tagName
            - soup.find('tagName',class_='') #class_ 加下划线区别关键字
        soup.find_all('tagName'):返回符合要求的所有标签(列表)
        soup.select('某种选择器id,class,标签，层级...选择器')，返回的是一个列表 #前端选择器
        -获取标签之间的文本数据 #定位标签之后
            soup.a.text/string/get_text()
            text/get_text()可以获取某一个标签中所有的文本内容
            string 只可以获取改标签直系的文本内容
        -获取标签中的属性值
            soup.a['href']
    xpath 重点 --最常用且最便捷高效的一种解析方式。通用型。 xpath表达式中出现“tbody”标签需要删除，否则异常♥♥♥♥♥♥
        -xpath解析原理：
            -1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
            -2.调用etree对象中的xpath方法结合xpath表达式实现标签的定位和内容的捕获
        -环境的安装
            -pip install lxml 安装lxml解析器
        -如何实例化一个etree对象：from lxml import etree
            -1.将本地的html文档中的源码数据加载到etree对象中：
                etree.parse(filepath)
            -2.可以讲从互联网上获取的源码数据加载到该对象中
                etree.HTML('page_text')
            -xpath('xpath表达式')
                - /：表示从根节点开始定位，表示的是一个层级
                - //：表示的是多个层级，可以表示从任意位置开始定位
                - 属性定位：//div[@class="layout qq-top cf"] tag[@attrName="attr"Value]
                - 索引定位：//div[@class="weatherMoreFutureCon"]/p[1] 索引是从1开始
                - 取文本：
                    - /text() 获取的是标签中直系的文本内容
                    - //text() 获取的是标签中所有的文本内容 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
                - 取属性：
                    - /@attrName  ==>img/@src
                - 高级应用：管道符增强xpath表达式通用性 “|”  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
                    li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    ### cookies 模拟登录
        没有请求到对应页面数据的原因
        - http/https : 无状态 （不知道发出的请求是否是登录状态）
        - cookie ： 用来让服务器端记录客户端的相关状态
            -手动cookie处理：抓包获取cookie值，封装到headers，不建议使用
            headers = {
                'Cookie':'XXX'
            }
            -自动cookie处理
                -cookie值的来源：模拟登录post请求后由服务器端创建 Set-Cookie
                -session会话对象：
                    - 作用：
                        1.可以进行请求的发送。
                        2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中。
                -创建一个session对象：session = requests.Session()
                -使用session对象进行模拟登录post请求的发送（cookie会被存储在session中）
                -使用session对象进行get请求发送 （携带cookie）

    ### 代理： 破解封IP这种反爬机制
            - 代理即 代理服务器
            - 突破自身IP访问的限制。（反反爬策略）
            - 隐藏自身真实的IP，免受攻击
        代理相关的网站：
            - 快代理
            - 西祠代理
            - www.goubanjia.com
        代理IP的类型：
            - http: 应用到http协议对应的url中
            - https:应用到https协议对应的url中
        代理IP的匿名度：
            - 透明：服务器知道该次请求使用了代理，也知道请求对应的真实IP
            - 匿名：知道使用了代理，不知道真实IP
            - 高匿：不知道使用了代理，更不知道真实IP
        使用
            - get/post请求参数 增加字典proxies = {"https":"IP:端口"}
    #高性能异步爬虫
        - 目的：在爬虫中使用异步实现高性能的数据爬取操作
    异步爬虫的方式
        - 多线程/多进程（不建议）：
            好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行
            弊端：无法无限制的开启多线程或者多进程
        - 线程池/进程池（适当使用）：
            好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好地降低系统的开销
            弊端：池中线程或进程的数量是有上限的
        - 单线程+异步协程（推荐）：
            event_loop:事件循环，相当于一个无限循环，可以把一些函数注册到这个事件循环上，当满足某些条件时，函数就会被循环执行
            coroutine:协程对象，可以讲协程对象注册到事件循环中，它会被事件循环调用。
            async：关键词 定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。
            task：任务 它是对协程对象的进一步封装，包含了任务的各个状态
            future：代表将来执行或还没有执行的任务，实际和task没有本质区别
            await：用来挂起阻塞方法的执行
    #selenium模块在爬虫中的应用
        - 便捷地获取网站中动态加载的数据
        - 便捷实现模拟登录
    什么是selenium模块
        - 基于浏览器自动化的一个模块
    selenium使用流程：
        - 环境安装：pip install selenium
            - selenium：https://pypi.org/project/selenium/#description
        - 下载一个浏览器的驱动程序
            - Chrome：https://chromedriver.chromium.org/downloads
            - Edge：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
            - Firefox: https://github.com/mozilla/geckodriver/releases
                -geckodriver驱动对应： https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html
            - Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
        - 实例化一个浏览器对象 driver = webdriver.Edge() --> 获取页面源码数据 page_text = driver.page_source
        - 编写基于浏览器自动化的操作代码
            - 发起请求：get(url)
            - 标签定位：find
            - 标签交互：send_keys('xxx')/click()
            - 执行js程序：execute_script('jsCode')
            - 前进、后退：forward()、back()
            - 关闭浏览器：quit()
        - selenium处理iframe
            - 如果定位的标签存在于iframe标签之中，必须使用switch_to.frame('id')
            - 动作链: 导入 from selenium.webdriver import ActionChains --> 实例化 action = ActionChains(driver)
            - action.click_and_hold(element) 长按且点击
            - move_by_offset(x,y) 按水平X，垂直Y 移动多少像素
            - perform()立即执行动作链操作
            - action.release() 释放动作链
        - 无可视化界面（无头浏览器） phantomJs(停止更新)
    #scrapy框架
        - 什么是框架
            - 就是一个集成了很多功能并且具有很强通用性的一个项目模板
        - 如何学习框架
            - 专门学习框架封装的各种功能的详细用法
        - 什么是scrapy
            - 爬虫中封装好的一个明星框架
            - 功能：高性能的持久化存储，异步的数据下载，高性能的数据解析操作，分布式
        - scrapy框架的基本使用
            - 环境的安装：
                - mac or linux：pip install scrapy
                - win： ① pip install wheel
                        ②下载twisted，下载地址为：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
                        ③安装twisted：pip install Twisted...
                        ④pip install pywin32
                        ⑤pip install scrapy -------新版本直接执行此步骤即可
                        测试：在终端里录入scrapy指令，没有报错即表示安装成功
            - 创建一个工程： scrapy startproject xxx  --> scrapy startproject firstBlood
            - cd xxx ---> cd firstBlood
            - 在spiders子目录下创建一个爬虫文件
                - scrapy genspider spiderName www.xxx.com -->scrapy genspider first www.xxx.com
            - 执行工程：
                - scrapy crawl spiderName --> scrapy crawl first
                    - scrapy crawl first --nolog 无日志输出，不建议使用，看不到错误日志信息
                    - settings 中设置LOG_LEVEL = 'ERROR'，只显示ERROR级别的日志信息
            - settings.py
                - USER_AGENT --> UA伪装 value
                - ROBOTSTXT_OBEY --> False
            - 数据解析：
                extract() 可以将Selector对象中data参数存储的字符串提取出来
                列表调用了extract()之后，则表示将列表中没一个Selector对象中data对应的字符串提取出来, [content = ''.join(content)] --> 将拿到的列表转成字符串
                extract_first() 列表中第0个元素进行extract()操作
            - scrapy持久化存储：
                - 基于终端指令：
                    - 要求： 只可以将parse方法的【返回值】存储到本地的文本文件中
                    - scrapy crawl spiderName -o filepath  [./spiders 路径下执行]
                    - 注意：持久化存储对应的文本类型有限制 json/csv/xml/... 不包含txt
                    - 简介高效，但局限性强（数据只可以存储到指定后缀的文本文件中）
                - 基于管道： 重心
                    - 编码流程：
                        - 数据解析
                        - 在item类中定义相关的属性 items.py
                        - 将解析的数据封装存储到item类型的对象
                        - 将item类型的对象提交给管道进行持久化存储的操作 pipelines.py
                        - 在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
                        - 在配置文件中开启管道
                            #ITEM_PIPELINES = {
                            #    "threekingdoms.pipelines.ThreekingdomsPipeline": 300, #300表示的是优先级，数值越小优先级越高
                            #}
                    - 好处：
                        - 通用性强
                    - 缺点：
                        - 编码较为繁琐
        -* 面试题： 将爬取的数据一份存储到本地一份存储到数据库，如何实现？
            - 管道文件中一个管道类对应的是将数据存储到一种平台
            - 爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
            - process_item 中的 return item 表示将item传递给下一个即将被执行的管道类
            - 在配置文件中开启管道
                #ITEM_PIPELINES = {
                #   "threekingdoms.pipelines.ThreekingdomsPipeline": 300,
                #   "threekingdoms.pipelines.mysqlPileLine": 301,
                #    #300表示的是优先级，数值越小优先级越高
                #}
        - 基于Spider的全站数据爬取
            - 就是将网站中某板块下的全部页码对应的页面数据进行爬取
            - 需求：爬取某网站的图片名称
            - 实现方式：
                - 将所有页面的url添加到start_urls列表（不推荐）
                - 自行手动进行请求发送 callback回调函数专门用作于数据解析
                    - yield scrapy.Request(url= , callback = self.parse)
        - 五大核心组件
            引擎（Scrapy）
                用来处理整个系统的数据流处理，触发事务（框架核心）
            调度器（Scheduler）
                用来接受引擎发过来的请求，压入队列中，并在引擎再次请求的时候返回，可以想象成一个URL（抓取网页的网址或者说是链接）的优先队列，由它决定下一个要抓取的网址是什么，同时去除重复的网址
            下载器（Downloader）
                用于下载网页内容，并将网页内容返回给蜘蛛（Scrapy下载器是建立在twisted这个高效的异步模型上的）
            爬虫（Spiders）
                爬虫是主要干活的，用于从特定的网页中提取自己需要的信息，即所谓的实体（Item）。用户也可以从中提取出链接，让Scrapy继续抓取下一个页面
            项目管道（Pipeline）
                负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清楚不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
        -* 请求传参
            - 使用场景： 如果爬取解析的数据不在同一章页面中。（深度爬取）
            - 需求：爬取boss的岗位名称，岗位描述 （待实现，cookie、AJAX问题）
                    https://dianyi.ng/v/dianying.html 电影先生 爬取电影名称、剧情简介
        - 图片数据爬取之ImagesPipeline
            - 基于scrapy爬取字符串类型的数据和爬取图片类型的数据区别？
                - 字符串：只需要基于xpath进行解析且提交管道进行持久化存储
                - 图片：xpath解析出图片src的属性值。单独的对图片地址发起请求获取图片二进制类型的数据
            - ImagesPipeline
                - 只需要将img的src的属性值进行解析，封装到item，提交到管道，管道就会对图片的src进行请求发送获取图片的二进制类型的数据，且还会帮我们进行持久化存储。
            - 需求：爬取站长素材中的高清图片  https://sc.chinaz.com/tupian/
            - 使用流程：
                - 数据解析（图片的地址）
                - 将存储图片地址的item提交到指定的管道类
                - 在管道文件中定制一个基于ImagesPipeLine的一个管道类
                    - get_media_requests     #可以根据图片地址进行图片数据的请求
                    - file_path    #指定图片存储的路径
                    - item_completed   # 返回给下一个即将被执行的管道类
                - 在配置文件中
                    - IMAGES_STORE = './imgs'   #指定图片存储的目录
                    - 指定开启的管道：自定制的管道类
                    ITEM_PIPELINES = {
                           "imgsPro.pipelines.imgsPipeline": 300,
                        }
        - 中间件
            - 下载中间件
                - 位置：引擎和下载器之间
                - 作用：批量拦截到整个工程中所有的请求和响应
                - 拦截请求：
                    - UA伪装 在配置文件中的操作是全局的 process_request
                    - 代理IP process_exception -- return request
                - 拦截响应：
                    - 篡改响应数据，响应对象
                    - 需求：爬取网易新闻中的新闻数据（标题和内容）
                        - 1.通过网易新闻的首页解析出五大板块对应的详情页的url（没有动态加载）
                        - 2.每一个板块对应的新闻标题都是动态加载出来的（动态加载）
                        - 3.通过解析出每一条新闻详情页的url获取详情页的页面源码，解析出新闻内容
        - CrawlSpider:类，Spider的一个子类
            - 全站数据爬取的方式
                - 基于Spider：手动请求发送
                - 基于CrawlSpider
            - crawlSpider的使用：
                - 创建一个工程
                - cd XXX
                - 创建爬虫文件（CrawlSpider）：
                    - scrapy genspider -t crawl XXX www.xxx.com
                    - 链接提取器：
                        - 作用：根据指定规则进行指定链接的提取
                    - 规则解析器：
                        - 作用：将链接提取器提取到的链接进行指定规则（callback）的解析操作
                    - follow
                        - 作用：True -可以将链接提取器 继续作用到 链接提取器提取到的链接 所对应的页面
                #需求：爬取sun网站中的编号、标题、内容，编号
                    - 分析：爬取的数据没有在同一章页面
                    - 1. 可以使用链接提取器提取所有的页码链接
                    - 2. 让链接提取器提取所有的详情页的链接

#分布式爬虫
    - 概念： 我们需要搭建一个分布式的机群，让其对一组资源进行分布联合爬取
    - 作用： 提升爬取数据的效率
    - 如何实现分布式？
        - 安装 scrapy-redis 组件
        - 原生的scrapy是不可以实现分布式爬虫，必须要让scrapy结合这scrapy-redis组件一起实现分布式
        - 为什么原生不可以实现分布式爬虫
            - 调度器不可以被分布式机群共享
            - 管道不可以被分布式机群共享
        - scrapy-redis组件的作用：
            - 可以给原生的scrapy框架提供可以被共享的管道和调度器
        - 实现流程
            - 创建一个工程
            - 创建一个基于CrawlSpider的爬虫文件（全站爬虫更便捷）
            - 修改当前的爬虫文件：
                - 导包： from scrapy_redis.spiders import RedisCrawlSpider
                - 将start_urls 和 allowed_domains进行注释
                - 添加一个新属性：redis_key = 'sun' 可以被共享的调度器队列的名称
                - 编写数据解析相关的操作
                - 将当前爬虫类的父类修改成RedisCrawlSpider
            - 修改配置文件settings
                - 指定使用可以被共享的管道
                    ITEM_PIPELINES = {
                        'scrapy_redis.pipelines.RedisPipeline':400
                    }
                - 指定调度器
                    #增加一个去重容器类的配置，作用使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化存储
                    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
                    #使用scrapy-redis组件自己的调度器
                    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
                    #配置调度器是否要持久化，也就是当爬虫结束了，要不要清空Redis中请求队列和去重指纹的set。如果是True，只爬取没有爬过的数据。
                    SCHEDULER_PERSIST = True
                - 指定redis服务器，不指定则默认本机
                    REDIS_HOST = '127.0.0.1' #redis远程服务的ip地址（修改）
                    REDIS_PORT = 6379
            - redis相关操作配置：
                - 配置redis的配置文件：redis.conf
                    - linux或者mac：redis.conf
                    - windows：redis.windows.conf
                    - 打开配置文件修改
                        - 将bind 127.0.0.1 默认绑定注释掉
                        - 关闭保护模式: protected-mode yes ---> no
                    - 结合着配置文件开启redis服务
                        - redis-server 配置文件（redis.conf/redis.windows.conf）
                    - 启动客户端
                        - redis-cli
            - 执行工程：
                - scrapy runspider xxx.py
            - 向调度器的队列中放入一个起始的url
                - 调度器的队列在redis的客户端中
                    - lpush xxx www.xxx.com
            - 存储在 redis 的proName：items
                -keys * ---> lrange XXX 0 -1
#增量式爬虫
    - 概念： 监测网站数据更新的情况，只会爬取网站最新更新出来的数据。
    - 分析：
        - 指定一个起始url
        - 基于CrawlSpider获取其他页码链接
        - 基于Rule将其他页码链接进行请求
        - 从每一个页码对应的页码源码中解析出每一个电影详情页的url

        - 核心：检测电影详情页的URL之前有没有请求过
            - 将爬取过的电影详情页的URL存储
                - 存储到redis的set数据结构
                    #创建redis链接对象
                    conn = Redis(host='127.0.0.1',port=6379)
                        #将详情页的url存入redis的set中
                        ex = self.conn.sadd('urls',detail_url)
                        if ex == 1:
                            print('该URL未爬取过，可以进行数据的爬取')
                            yield scrapy.Request(url = detail_url,callback=self.parse_detail)
                        else:
                            print('数据还未更新，暂无新数据可爬取')
        - 对详情页的url发起请求，然后解析出电影的名称和简介
        - 进行持久化存储