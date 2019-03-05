# -*- coding: utf-8 -*-
import scrapy


class QhSpider(scrapy.Spider):
    name = 'qh_spider'
    allowed_domains = ["yz.tsinghua.edu.cn"]
    start_urls = ['http://yz.tsinghua.edu.cn/']

    def parse(self, response):
        pass
