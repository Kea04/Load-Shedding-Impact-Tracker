import sys
import time
import schedule
from src.extract import extract_all
from src.transform import parse_all
from src.mock_data import generate_mock_dataset
from src.load import load_clean
from src.db import init_db
from config.config import AREAS

def run_pipeline(use_mock=False):
    print("Running pipeline...")

    if use_mock:
        print("Using mock data (no API calls)")
        events = generate_mock_dataset(AREAS.keys())
    else:
        records = extract_all()
        events = parse_all(records)

    for event in events:
        load_clean(event)
    print(f"Pipeline finished. Loaded {len(events)} outage events.")

if __name__ == "__main__":
    use_mock = "--mock" in sys.argv
    init_db()
    run_pipeline(use_mock=use_mock)

    if not use_mock:
        schedule.every(6).hours.do(run_pipeline)
        while True:
            schedule.run_pending()
            time.sleep(60)