import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'elements'
    allowed_domains = ['elementshk.com/']
    start_urls = ['https://www.elementshk.com/eng/elements/shopInfo/list']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        Title = response.css('div.shopsearchtable td.td1::text').extract()
        No = response.css('div.shopsearchtable td.td2::text').extract()
        Tel = response.css('div.shopsearchtable td.td3::text').extract()
        Cat = response.css('div.shopsearchtable td.td4::text').extract()
        Zone = response.css('div.shopsearchtable td.td5::text').extract()

        for Title, No, Tel, Cat, Zone in zip(Title, No, Tel, Cat,Zone):
            i = {}
            i['Title'] = Title
            i['No'] = No
            i['Tel'] = Tel
            i['Cat'] = Cat
            i['Zone'] = Zone
            yield i