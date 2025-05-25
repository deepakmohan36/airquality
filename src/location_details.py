import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

def get_location_data(location_id):
    max_retries = 5
    backoff = 1  

    URL = f"https://api.openaq.org/v3/locations/{location_id}"
    API_KEY = os.environ.get("OPENAQ_API_KEY")
    
    header = {
        "X-API-Key": API_KEY
    }

    for attempt in range(max_retries):
        response = requests.get(URL, headers=header)

        if response.status_code == 429:
            print(f"Rate limit hit for location {location_id}. Sleeping for {backoff} seconds...")
            time.sleep(backoff)
            backoff *= 2 
            continue

        response.raise_for_status()
        result = response.json()
        return result.get("results", [])

    print(f"Failed to fetch data for location {location_id} after {max_retries} attempts.")
    return []

def get_location_details_for_multiple_locations(location_ids):
    all_data = []
    for loc_id in location_ids:
        data = get_location_data(loc_id)
        if data:
            all_data.append(data)
        time.sleep(1)  
    return all_data


# #sample 
# location_ids = ["8118", "8726", "10293"]  
# air_quality_data = get_location_details_for_multiple_locations(location_ids)
# print(air_quality_data)
