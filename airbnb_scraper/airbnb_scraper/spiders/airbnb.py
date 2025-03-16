import scrapy
import json
import requests

class AirbnbSpider(scrapy.Spider):
    name = "airbnb"
    start_urls = ["https://www.airbnb.com/s/New-York--NY--United-States/homes"]

    def parse(self, response):
        listings = response.css("div._gig1e7")
        for listing in listings:
            data = {
                "title": listing.css("span._bzh5lkq::text").get(),
                "location": "New York, USA",
                "price_per_night": listing.css("span._tyxjp1::text").re_first(r"\$(\d+)"),
                "ratings": listing.css("span._10fy1f8::text").get(),
                "num_reviews": listing.css("span._a7a5sx::text").get(),
                "image_urls": [listing.css("img::attr(src)").get()],
                "description": "Cozy home",
                "amenities": ["WiFi", "Kitchen"],
                "host_info": {},
                "property_type": "Apartment"
            }
            
            requests.post("http://127.0.0.1:8000/api/listings/", json=data)

