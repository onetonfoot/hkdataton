# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'domain'
    allowed_domains = ['domain-mall.hk/']
    start_urls = ['http://www.domain-mall.hk/index.php/shopping-directory']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        #l = response.css('.sp_list')
        title =  response.css('td.shop-name::text').extract()
        shopno = response.css('td.shop-number::text').extract()
        floor = response.css('td.shop-floor::text').extract()
        tel = response.css('td.shop-tel::text').extract()
    

        for title, shopno, floor, tel in zip(title, shopno, floor, tel):
            i = {}
            i['title'] = title
            i['shopno'] = shopno
            i['floor'] = floor
            i['tel'] = tel

            yield i
        #tel missing value issue
