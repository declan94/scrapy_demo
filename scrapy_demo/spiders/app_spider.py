# -*- coding: utf-8 -*-
import scrapy


class AppSpiderSpider(scrapy.Spider):
    name = 'app_spider'
    allowed_domains = ['play.google.com']
    start_urls = ['http://play.google.com/']

    def parse(self, response):
        pass
