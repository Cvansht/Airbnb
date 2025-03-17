# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import requests

class AirbnbScraperPipeline:
    def process_item(self, item, spider):
        # Send data to Django API
        requests.post("http://127.0.0.1:8000/api/listings/", json=item)
        return item

