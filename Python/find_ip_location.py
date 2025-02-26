import requests
from dotenv import load_dotenv
import os
import sys
import json

load_dotenv()

ip_api_key=os.getenv("IP_API_KEY").strip()
target_file = "geolocation_data.json"

if len(sys.argv) != 2:
    print("Usage: python3 find_ip_location.py <IP_ADDRESS>")
    sys.exit(1)

ip_address = sys.argv[1]
url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={ip_api_key}&ip_address={ip_address}"
print(url)
response = requests.get(url)
print(response.content)

if response.status_code == 200:
    data = response.json()
    result = {
        "IP": data.get("ip_address"),
        "City": data.get("city"),
        "Region": data.get("region"),
        "Zipcode": data.get("postal_code"),
        "Country": data.get("country"),
        "Longitude": data.get("longitude"),
        "Latitude": data.get("latitude"),
        "Internet Service Provider": data.get("connection", {}).get("autonomous_system_organization")
    }

    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(result)

    with open(target_file, "a", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False) 
    
    print(f"Data saved to {target_file}")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")