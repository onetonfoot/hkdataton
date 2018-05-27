# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'k11'
    allowed_domains = ['hk.k11.com/']
    start_urls = ['http://hk.k11.com/list/shop']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        #l = response.css('.sp_list')
        title =  response.css('span.shopName::text').extract()
        location = response.css('span.shopLocation::text').extract()
        tel = response.css('span.tel_holder .shopTel [href]::text').extract()
    
        for title, location, tel in zip(title, location, tel):
            i = {}
            i['title'] = title
            i['location'] = location
            i['tel'] = tel

            yield i

