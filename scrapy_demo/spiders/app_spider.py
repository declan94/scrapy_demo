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
        detail_relative_url = response.css("a.card-click-target::attr(href)").extract_first()
        detail_url = response.urljoin(detail_relative_url)
        yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta=response.meta)

    def parse_detail(self, response):
        app = {}
        app["name"] = response.meta["app_name"]
        app["crawled_name"] = response.css("h1[itemprop='name'] span::text").extract_first()
        app["icon_url"] = response.css("img.T75of[itemprop='image']::attr(src)").extract_first()
        category_url = response.css("a[itemprop='genre']::attr(href)").extract_first()
        if category_url:
            app["category"] = category_url.split("/")[-1]
        app["desc"] = response.css("div[jsname='sngebd']::text").extract_first()
        print "\n" + str(app) + "\n"
