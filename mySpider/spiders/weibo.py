import scrapy
import json


class weibo(scrapy.Spider):
    # 必须写，后面需要通过爬虫名称启动爬虫
    name = "weibo"

    # 在这个方法中发起请求
    def start_requests(self):
        url = "https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0&since_id=1"

        # callback ： 回调函数，成功之后会执行
        yield scrapy.Request(url=url, callback=self.parse, method="get")

    # 回调函数，处理返回的数据
    def parse(self, response):
        print(response.text)

        # 将json的字符串转换成json对象
        js = json.loads(response.text)

        data = js["data"]
        # 所有微博的数组
        cards = data["cards"]

        for card in cards:
            mblog = card["mblog"]

            id = mblog["id"]

            text = mblog["text"]
            user = mblog["user"]
            reposts_count = mblog["reposts_count"]
            comments_count = mblog["comments_count"]
            attitudes_count = mblog["attitudes_count"]

            screen_name = user["screen_name"]

            follow_count = user["follow_count"]
            followers_count = user["followers_count"]
            gender = user["gender"]

            line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
                id, reposts_count, comments_count, attitudes_count, screen_name, gender, follow_count, followers_count,
                text)

            print(line)
