# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from settings import CLOSESPIDER_ITEMCOUNT
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
class CrawlersPipeline(object):

	#def __init__(self):
	#	dispatcher.connect(self.spider_closed, signals.spider_closed)

	def process_item(self, item, spider):
		scrape_count = spider.crawler.stats.get_value('item_scraped_count')
		if scrape_count >= CLOSESPIDER_ITEMCOUNT:
			raise DropItem("Finished!")
		return item

