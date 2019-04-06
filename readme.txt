使用的技术：scrapy,selenium+chromdriver
目的：准备将伯乐在线网站的数据放到redis数据库

##单机爬虫
1.先导入需要的包 比如scrapy_redis.spiders import RedisSpider
2.注释掉start_urls 并添加redis_key
3.在setting 文件下配置redis_spider的信息
    # 3.1调度器：确保数据存储到redis中
    SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
    # 3.2确保所有的爬虫过滤掉重复的链接
    DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
    # 3.3设置redis的数据处理管道
    ITEM_PIPELINES = {
       'scrapy_redis.pipelines.RedisPipeline': 300,
    }
    # 3.4爬取一行，写入一行
    SCHEDULER_PERSIST = True
    # 安装redis服务器的ip地址
    REDIS_HOST = '10.54.243.98'
    # redis的端口
    REDIS_PORT = '6379'
##分布式爬虫
1.封装框架所需要的包
pip freeze > requirements.txt

2.在其他节点上安装这个项目所需要的模块
pip install -r requirements.txt
3,然后切换到爬虫环境目录下，scrapy runspider bole.py
