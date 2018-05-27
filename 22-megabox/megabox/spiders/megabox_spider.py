# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,Spider

class MegaboxSpiderSpider(scrapy.Spider):

    name = 'megabox'
    allowed_domains = ['www.megabox.com.hk/']
    start_urls = ['http://www.megabox.com.hk/shopping_directory.php?mid=&smc=S&scid=4&sid=']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        title = response.css(".details a::text").extract()
        # loc = response.css(".details p.location::text").extract()
        info = response.css(".details p::text").extract()
        link = response.css(".details ::attr(href)").extract()

        loc = []
        text = []
        for k in range(len(info)):
            if k%2:
                loc.append(info[k])
            else:
                text.append(info[k])

        for title, loc, text, link in zip(title, loc, text, link):
            i = {}
            i['title'] = title
            i['location'] = loc
            i['text'] = text
            i['link'] = link
            yield i

