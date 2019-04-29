#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 00:09:54 2019

@author: parsakon
"""
import scrapy
from scrapy import Request

class clSpyder(scrapy.Spider):
    name = "craigslist_spider" # Name the spider
    allowed_domains = ['craigslist.org']
    start_urls = ['https://losangeles.craigslist.org/d/real-estate/search/rea'] # pull data from this website
    
    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles:
            yield {'Title': title}
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)
