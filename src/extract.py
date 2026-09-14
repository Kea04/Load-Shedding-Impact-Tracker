import requests
import json
import logging
from datetime import datetime
from config.config import BASE_URL, HEADERS, AREAS

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_national_status():
    try:
        response = requests.get(f"{BASE_URL}/status", headers=HEADERS, timeout=10)
        response.raise_for_status()
        logging.info("Fetched national status")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch national status: {e}")
        return None

def fetch_area_schedule(area_id):
    try:
        response = requests.get(
            f"{BASE_URL}/area", headers=HEADERS,
            params={"id": area_id}, timeout=10
        )
        response.raise_for_status()
        logging.info(f"Fetched area schedule for {area_id}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch area {area_id}: {e}")
        return None

def save_raw(data, label):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{label}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    return filename

def extract_all():
    records = {"national": None, "areas": {}}
    national = fetch_national_status()
    if national:
        save_raw(national, "national_status")
        records["national"] = national

    for name, area_id in AREAS.items():
        area_data = fetch_area_schedule(area_id)
        if area_data:
            save_raw(area_data, f"area_{name}")
            records["areas"][name] = area_data
    return records

if __name__ == "__main__":
    result = extract_all()
    print(f"Fetched national status and {len(result['areas'])} area schedules")