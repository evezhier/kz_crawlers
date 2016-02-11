# -*- coding: utf-8 -*- 

import scrapy

scrapy.optional_features.remove('boto')

class InvestSpider(scrapy.Spider):
	name = "investspider"
	start_urls = ["http://investfunds.kz/news/markets/"]

	def parse(self, response):
		for link in response.xpath('//tr//a/@href').extract():
			url = response.urljoin(link)
			yield scrapy.Request(url, self.parse_article)
		next_page = response.css('.nav-links a::attr("href")').extract()[-1]
		print next_page
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), self.parse)

	def parse_article(self, response):
		item = CrawlersItem()
		item['link'] = response.url
		item['title'] = response.css('.block-header::text').extract()[1].strip()
		raw = response.css('.block-win.text-block').xpath(".//text()[normalize-space() and not(ancestor::script)]").extract()
		item['text'] = " ".join([r.strip() for r in raw])
		print(type(item['text']))
		return item

class DengiSpider(scrapy.Spider):
	name = "dengispider"
	start_urls = ["http://prodengi.kz/lenta/"]
	cur_page = 1

	def parse(self, response):
		for link in response.css('.list-news').xpath('.//h2/a/@href').extract():
			url = response.urljoin(link)
			yield scrapy.Request(url, self.parse_article)
		self.cur_page +=1
		next_page = "/lenta/?page={}".format(self.cur_page)
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), self.parse)

	def parse_article(self, response):
		item = CrawlersItem()
		item['link'] = response.url
		item['title'] = response.css('#content h1::text').extract()
		raw = response.css('.content').xpath(".//p//text()[normalize-space() and not(ancestor::script|ancestor::label)]").extract()
		item['text'] = " ".join([r.strip() for r in raw])
		return item