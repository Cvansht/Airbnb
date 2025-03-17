import scrapy
from airbnb_scraper.items import AirbnbScraperItem

class AirbnbSpider(scrapy.Spider):
    name = "airbnb"
    allowed_domains = ["airbnb.com"]
    start_urls = [
        "https://www.airbnb.com/s/New-York--NY/homes"  # Example URL, change dynamically later
    ]

    def parse(self, response):
        listings = response.css("div._gig1e7")

        for listing in listings:
            item = AirbnbScraperItem()
            item['title'] = listing.css("div._bzh5lkq::text").get()
            item['location'] = listing.css("div._1tanv1h::text").get()
            item['price_per_night'] = listing.css("span._tyxjp1::text").get()
            item['image_urls'] = listing.css("img._6tbg2q::attr(src)").getall()
            item['ratings'] = listing.css("span._10fy1f8::text").get()
            item['num_reviews'] = listing.css("span._a7a5sx::text").get()
            yield item
