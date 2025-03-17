import requests
import json

class AirbnbScraperPipeline:
    def process_item(self, item, spider):
        url = "http://127.0.0.1:8000/api/add_listing"  # Your Django API endpoint

        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(dict(item)), headers=headers)

        print(response.json())  # Debugging response
        return item
