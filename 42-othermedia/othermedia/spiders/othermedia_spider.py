# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,Spider
import re

class OthermediaSpiderSpider(scrapy.Spider):

    name = 'othermedia'
    allowed_domains = ['movie.yahoo-leisure.hk']
    start_urls = ['https://movie.yahoo-leisure.hk/cinema/details/20']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        title = response.css(".near-cinema-list ::text").extract()
        link = response.css(".near-cinema-list ::attr(href)").extract()

        p = re.compile('\r.*')
        dis = re.compile('(約|港島|九龍|新界)')
        title2 = []

        for k in title:
            if not p.match(k):
                if not dis.match(k):
                    title2.append(k)

        for title, link in zip(title2, link):
            i = {}
            i['title'] = title
            i['link'] = link
            yield i

        info = response.css(".cinema-info ::text").extract()
        info2 = []

        for k in info:
            if not p.match(k):
                info2.append(k)

        for info in info2:
            i = {}
            i['info'] = info
            yield i