# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'citywalk'
    allowed_domains = ['citywalk.com.hk']
    start_urls = ['http://www.citywalk.com.hk/site/mall_dir/en']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        l = response.css('.sp_list')
        title =  l.css('div [style^="width:48%; float:left"]::text').extract()
        loc = l.css('div [style^="float"]::text').extract()
    
        for title, loc in zip(title, loc):
            i = {}
            i['title'] = title
            i['location'] = loc

            yield i

