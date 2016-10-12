# -*- coding: utf-8 -*-
import scrapy


class MydomainSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["http://stackoverflow.com"]
    start_urls = (
        'http://stackoverflow.com/questions/39955418/spring-batch-read-write-in-the-same-table',
    )

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url,callback=self.parse_question)
            
    def parse_question(self,response):
        yield{
            'title':response.css('h1 a::text').extract()[0],
            'votes':response.css(".question .vote-count-post::text").extract()[0],
            'body':response.css(".question .post-text").extract()[0],
            'tags':response.css('.question .post-tag::text').extract()[0],
            'link':response.url,
            }
