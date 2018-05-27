# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,Spider

class AirSpider(scrapy.Spider):

    name = 'airpollution'
    allowed_domains = ['www.aqhi.gov.hk']
    start_urls = ['http://www.aqhi.gov.hk/tc.html']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        title = response.css(".tblCurrAQHI_tdName ::text").extract()
        link = response.css(".tblCurrAQHI_tdName ::attr(href)").extract()
        index = response.css(".tblCurrAQHI_tdBand ::text").extract()
        info = response.css(".tblCurrAQHI_tdBand ::attr(href)").extract()
        risk = response.css(".tblCurrAQHI_tdCate ::text").extract()

        # loc = []
        # text = []
        # for k in range(len(info)):
        #     if k%2:
        #         loc.append(info[k])
        #     else:
        #         text.append(info[k])

        for title, link, index, info, risk in zip(title, link, index, info, risk):
            i = {}
            i['title'] = title
            i['link'] = link
            i['index'] = index
            i['info'] = info
            i['risk'] = risk
            yield i
