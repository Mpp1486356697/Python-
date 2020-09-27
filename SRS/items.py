# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SrsItem(scrapy.Item):
    # define the fields for your item here like:

    # 地区
    name = scrapy.Field()
    # 确诊人数
    confirmeder = scrapy.Field()
    # 死亡人数
    dier = scrapy.Field()
    # 治愈人数
    curer = scrapy.Field()
    # 疑似人数
    # suspected = scrapy.Field()
    # #     截止时间
    # deadline = scrapy.Field()
