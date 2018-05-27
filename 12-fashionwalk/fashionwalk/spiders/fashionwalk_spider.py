# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'fashionwalk'
    allowed_domains = ['fashionwalk.com.hk/']
    start_urls = ['http://fashionwalk.com.hk/en/shoplist']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        l = response.css('div.shop-address::text').extract()
        title = l
        '''l =  response.css('div.shop-address::text').extract().split(',')
        s = []
        for x in l:
            y = x.split(',')
            s.append(y)
            return s
        title = s[0]
        loc1 = s[1]
        loc2 = s[2]
        loc3 = s[3]
        loc4 = s[4]'''
        
        for title in zip(title):
            i = {}
            i['title'] = title
            '''i['loc1'] = loc1
            i['loc2'] = loc2
            i['loc3'] = loc3
            i['loc4'] = loc4'''
            yield i

