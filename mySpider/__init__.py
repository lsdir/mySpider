from scrapy import cmdline

# 通过爬虫名启动爬虫
cmdline.execute("scrapy crawl weibo".split(" "))
