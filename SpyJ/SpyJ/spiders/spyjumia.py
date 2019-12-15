# -*- coding: utf-8 -*-
import scrapy


class SpyjumiaSpider(scrapy.Spider):
    name = 'spyjumia'
    allowed_domains = ['www.jumia.com.ng']
    start_urls = ['http://www.jumia.com.ng/']

    def parse(self, response):
        pass
