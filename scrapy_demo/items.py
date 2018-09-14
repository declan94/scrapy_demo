# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    crawled_name = scrapy.Field()
    category = scrapy.Field()
    icon_url = scrapy.Field()
    desc = scrapy.Field()
