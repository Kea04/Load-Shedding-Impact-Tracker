import requests
import json
from datetime import datetime
from config.config import BASE_URL, HEADERS

def fetch_national_status():
    url = f"{BASE_URL}/status"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def save_raw(data, label):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{label}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    return filename

if __name__ == "__main__":
    data = fetch_national_status()
    path = save_raw(data, "national_status")
    print(f"Saved raw status to {path}")