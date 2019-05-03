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
    
    def parseListing(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        price = response.meta.get('Price')
        location = response.meta.get('Location')
        date = response.meta.get('Date')
        
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())
        geoposition = response.xpath('//head/meta[@name="geo.position"]/@content').get()
        lat, long = geoposition.split(';',2)
        yield{'URL': url, 'Title': title, 'Description':description, 'Price':price, 'Location':location,'Date':date, 'Description':description,'Geoposition':geoposition, 'Latitude':lat, 'Longitude':long}

    def parse(self, response):
        listings = response.xpath('//p[@class="result-info"]')
        for listing in listings:
            title = listing.xpath('a/text()').extract_first()
            price = listing.xpath('span/span[@class="result-price"]/text()').extract_first()
            location = listing.xpath('span/span[@class="result-hood"]/text()').extract_first()
            relative_url = listing.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            date = listing.xpath('time/@title').extract_first()
            
            yield Request(absolute_url, callback=self.parseListing, meta={'URL':absolute_url,'Title':title,'Price':price,'Location':location,'Date':date})

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield Request(absolute_next_url, callback=self.parse)
    