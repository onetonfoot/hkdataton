import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule,Spider


class BotSpider(Spider):

    name = 'FestivalWalk'
    allowed_domains = ['festivalwalk.com.hk/']
    start_urls = ['http://www.festivalwalk.com.hk/en/shopping/index.php']

    rules = {
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    }

    def parse(self, response):
        title = response.css('div.text p::text').extract()

        for title in zip(title):
            i = {}
            i['title'] = title
            yield i