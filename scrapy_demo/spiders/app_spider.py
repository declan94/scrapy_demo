# -*- coding: utf-8 -*-
import scrapy


class AppSpiderSpider(scrapy.Spider):
    name = 'app_spider'
    allowed_domains = ['play.google.com']
    # start_urls = ['http://play.google.com/']

    def start_requests(self):
        with open("app_names.txt") as f:
            for app_name in f.readlines():
                app_name = app_name.strip()
                url = "https://play.google.com/store/search?c=apps&q=" + app_name
                yield scrapy.Request(url=url, callback=self.parse_search, meta={"app_name": app_name})

    def parse_search(self, response):
        with open(response.meta["app_name"] + ".html", "w") as f:
            f.write(response.body)
