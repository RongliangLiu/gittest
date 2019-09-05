# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from mspider.items import MspiderItem

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

class MusicspiderSpider(scrapy.Spider):
    name = 'musicSpider'
    allowed_domains = ['htqyy.com']
    start_urls = ['http://www.htqyy.com/top/musicList/hot?pageIndex=0'
                  '&pageSize=20']

    def parse(self, response):
        # filename = "music.html"
        data1 = response.body
        # open(filename, "wb").write(data)

        titles = re.findall(r'title="(.*?)" sid', data1)
        id_list = re.findall(r'href="/play/(.*?)" target="play"', data1)


        for i in range(0, len(titles)):
            songurl = "http://f2.htqyy.com/play7/" + str(id_list[i]) + "/mp3/9"
            songname = titles[i]

            data2 = requests.get(songurl).content
            item = MspiderItem
            item["data"] = data2
            yield item