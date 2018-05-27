# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,Spider


class BotSpider(Spider):

    name = 'ifc'
    allowed_domains = ['ifc.com.hk/']
    start_urls = ['http://ifc.com.hk/en/mall/shopping/']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        title = response.css(".row .title::text").extract()
        loc = response.css(".row .location::text").extract()
        info = response.css(".row .info::text").extract()
        tel = response.css(".row ::attr(href)").extract()

        for title, loc, info, tel in zip(title, loc, info, tel):
            i = {}
            i['title'] = title
            i['location'] = loc
            i['info'] = info
            i['tel'] = tel
            yield i

        # for k in range(len((response.css(".row .title::text").extract()))):
        #     # vari = response.css(".row .title::text").extract()
        #     i ={}
        #     i['title'] = response.css(".row .title::text").extract()[k]
        #     i['location'] = response.css(".row .location::text").extract()[k]
        #     i['info'] = response.css(".row .info::text").extract()[k]
        #     i['tel'] = response.css(".row ::attr(href)").extract()[k]
        #     yield i
        #
