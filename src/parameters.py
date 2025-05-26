import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

def get_all_parameters():
    URL = "https://api.openaq.org/v3/parameters"
    API_KEY = os.environ.get("OPENAQ_API_KEY")
    
    headers = {
        "X-API-Key": API_KEY
    }

    all_data = []
    # ids = []

    page = 1
    limit = 100

    while True:
        params = {
            "page": page,
            "limit": limit
        }

        response = requests.get(URL, headers=headers, params=params)

        if response.status_code == 429:
            print("Rate limit hit. Sleeping for 10 seconds...")
            time.sleep(10)
            continue

        response.raise_for_status()
        result = response.json()

        data = result.get("results", [])
        if not data:
            break

        all_data.extend(data)
        # ids.extend([item["id"] for item in data])

        if len(data) < limit:
            break

        page += 1
        time.sleep(1)  # Small pause to reduce risk of rate limiting

    return all_data

print(get_all_parameters())
