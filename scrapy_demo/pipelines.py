# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import unicodecsv as csv

class SaveCsvPipeline(object):
    
    def open_spider(self, spider):
        self.file = open('app_items.csv', 'w')
        self.writer = csv.DictWriter(self.file, fieldnames=["name", "crawled_name", "category", "icon_url", "desc"])
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item