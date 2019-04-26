# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class HallobotoSpider(scrapy.Spider):
    name = 'halloboto'
    allowed_domains = ['halooglasi.com']

    start_urls = ["https://www.halooglasi.com/nekretnine/prodaja-stanova/centar-novogradnja-garaza/5425634579883?kid=4&sid=1556141851573",]

    def start_requests(self):
        script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(1))

            assert(splash:runjs('document.getElementsByClassName("show-phone-numbers")[0].click()'))
            assert(splash:wait(1))

            -- return result as a JSON object
            return {
                html = splash:html()
            }
        end
        """
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'args': {'lua_source': script},
                    'endpoint': 'execute',
                }
            })

    def parse(self, response):       
        print(response.css('h1.ad-details-title span::text').get())
        print(response.css('span.offer-price span::text').get()) 
        print(response.xpath('//*[@id="plh53"]/a/text()').get())
        print(response.xpath('//*[@id="plh54"]/a/text()').get())
       
