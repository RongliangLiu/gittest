# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from mspider.musicSpider import parse
import random

class MspiderPipeline(object):
    # def __init__(self):
    #     self.filename = open("{}.mp3".format(songname), "a")
    # songname = parse
    # songname["songnema"] = songname
    def process_item(self, item, spider):
        with open("D:\\music.mp3".format(range(0, 100)), "wb") as f:
            f.write(item)

        return item

    # 当爬取结束时执行的方法
    def close_spider(self, spider):
        self.spider.close()

