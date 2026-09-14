import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("ESP_TOKEN")
BASE_URL = "https://developer.sepush.co.za/business/3.1"
HEADERS = {"token": API_TOKEN}

AREAS = {
    "Rosebank": "za_gt_jhb_rosebank_gw5e",
    "Roodepoort": "za_gt_jhb_roodepoort_ddf1",
    "Fourways": "za_gt_jhb_fourways_4pef",
}

DB_PATH = "data/loadshedding.db"