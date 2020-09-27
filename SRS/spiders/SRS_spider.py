# -*- coding: utf-8 -*-
import scrapy
from SRS.items import SrsItem
from scrapy_splash import SplashRequest
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from scrapy.http import Request, HtmlResponse
from scrapy.selector import Selector
from scrapy_splash import SplashRequest


class SrsSpiderSpider(scrapy.Spider):
    name = 'SRS_spider'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1']

    # request需要封装成SplashRequest
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url
                                , self.parse
                                , args={'wait': '0.5'}
                                # ,endpoint='render.json'
                                )

    def parse(self, response):
        site = Selector(response)
        data_list = site.xpath("/html/body/div[2]/div/div/div/section/div[2]/div[6]/div[2]/table/tbody/tr")
        for i_item in data_list:
            SRS_item = SrsItem()
            SRS_item["name"] = i_item.xpath(
                "./td[@class='VirusTable_1-1-83_MdE8uT']/div/span[2]/text()").extract_first()
            SRS_item["confirmeder"] = i_item.xpath("./td[@class='VirusTable_1-1-83_3x1sDV']/text()").extract_first()
            SRS_item["curer"] = i_item.xpath("./td[3]/text()").extract_first()
            SRS_item["dier"] = i_item.xpath("./td[4]/text()").extract_first()
            if SRS_item["name"] is None:
                continue
            if SRS_item["curer"] == '-':
                SRS_item["curer"] = 0
            if SRS_item["dier"] == '-':
                SRS_item["dier"] = 0

            yield SRS_item
