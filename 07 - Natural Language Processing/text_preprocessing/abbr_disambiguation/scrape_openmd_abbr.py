#!/usr/bin/env python3

'''
Scrape OpenMD Medical Abbreviations
'''    
import scrapy

class OpenMDAbbrScraper(scrapy.Spider):
    name = "OpenMDAbbr"
    
    start_urls = [
        'https://openmd.com/dictionary/abbreviations/a',
        'https://openmd.com/dictionary/abbreviations/b',
        'https://openmd.com/dictionary/abbreviations/c',
        'https://openmd.com/dictionary/abbreviations/d',
        'https://openmd.com/dictionary/abbreviations/e',
        'https://openmd.com/dictionary/abbreviations/f',
        'https://openmd.com/dictionary/abbreviations/g',
        'https://openmd.com/dictionary/abbreviations/h',
        'https://openmd.com/dictionary/abbreviations/i',
        'https://openmd.com/dictionary/abbreviations/j',
        'https://openmd.com/dictionary/abbreviations/k',
        'https://openmd.com/dictionary/abbreviations/l',
        'https://openmd.com/dictionary/abbreviations/m',
        'https://openmd.com/dictionary/abbreviations/n',
        'https://openmd.com/dictionary/abbreviations/o',
        'https://openmd.com/dictionary/abbreviations/p',
        'https://openmd.com/dictionary/abbreviations/q',
        'https://openmd.com/dictionary/abbreviations/r',
        'https://openmd.com/dictionary/abbreviations/s',
        'https://openmd.com/dictionary/abbreviations/t',
        'https://openmd.com/dictionary/abbreviations/u',
        'https://openmd.com/dictionary/abbreviations/v',
        'https://openmd.com/dictionary/abbreviations/w',
        'https://openmd.com/dictionary/abbreviations/x',
        'https://openmd.com/dictionary/abbreviations/y',
        'https://openmd.com/dictionary/abbreviations/z'
    ]

    def parse(self, response):
        for row in response.xpath('//table//tr[position()>1]'):
            yield {
                'abbr': row.xpath('td[1]//text()').extract(),
                'full': row.xpath('td[2]//text()').extract(),
            }
            
"""
# generate url links           
import string
            
alphabet = list(string.ascii_lowercase)     # list letters of alphabet
for letter in alphabet:
    url = "\'https://openmd.com/dictionary/abbreviations/"+letter+"\',"
    print(url)
"""