import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.come'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']
    
    rule = (
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
        )
    
    def parse_item(self,response):
        self.log('Hi,this is an item page!%s' % response.url)
        
        item = scarpy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item