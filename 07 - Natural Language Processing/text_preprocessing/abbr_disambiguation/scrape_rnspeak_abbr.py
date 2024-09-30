#!/usr/bin/env python3

'''
Scrape Nursing Speak Abbreviations webpage for common nursing abbreviations
'''    
import scrapy


class NurseSpeakAbbrScraper(scrapy.Spider):
    name = "nurseAbbr"
    start_urls = ['https://rnspeak.com/nursing-abbreviations/']

    def parse(self, response):
        for row in response.xpath('//table//tr[position()>1]'):
            yield {
                'abbr': row.xpath('td[1]//text()').extract(),
                'full': row.xpath('td[2]//text()').extract(),
            }