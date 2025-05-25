import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_airquality_data(location_id):

    URL = f"https://api.openaq.org/v3/locations/{location_id}"
    API_KEY = os.environ.get("OPENAQ_API_KEY")
    
    header = {
        "X-API-Key":API_KEY
    }

    response = requests.get(URL, headers=header)

    result = response.json()

    data = result["results"]

    return data
