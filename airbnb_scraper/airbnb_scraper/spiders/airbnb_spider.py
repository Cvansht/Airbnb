import scrapy
from airbnb_scraper.items import AirbnbScraperItem
from scrapy_selenium import SeleniumRequest

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random

class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    start_urls = ['https://www.airbnb.com/s/Paris--France/homes']
    PROXIES = [
        'http://proxy1:port',
        'http://proxy2:port',
        # Add your proxy list here
    ]

    def get_driver(self, proxy):
        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy}')
        # Optional: Run headless to reduce resource use
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(
            service=Service('/path/to/chromedriver'),  # Update with your chromedriver path
            options=chrome_options
        )
        return driver

    def start_requests(self):
        for url in self.start_urls:
            proxy = random.choice(self.PROXIES) if self.PROXIES else None
            yield SeleniumRequest(
                url=url,
                wait_time=5,
                callback=self.parse,
                meta={'proxy': proxy},  # Pass proxy to middleware (optional)
                driver=self.get_driver(proxy)  # Custom driver with proxy
            )

    def parse(self, response):
        # Extract data from response.text
        listings = response.css('div[itemprop="itemListElement"]')
        for listing in listings:
            title = listing.css('div._1xzimi1::text').get()
            yield {'title': title}

        for listing in listings:
            item = AirbnbScraperItem()
            item['title'] = listing.css("div._bzh5lkq::text").get()
            item['location'] = listing.css("div._1tanv1h::text").get()
            item['price_per_night'] = listing.css("span._tyxjp1::text").get()
            item['image_urls'] = listing.css("img._6tbg2q::attr(src)").getall()
            item['ratings'] = listing.css("span._10fy1f8::text").get()
            item['num_reviews'] = listing.css("span._a7a5sx::text").get()
            yield item
