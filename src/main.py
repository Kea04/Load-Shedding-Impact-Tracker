import time
import schedule
from src.extract import extract_all
from src.transform import parse_all
from src.load import load_clean
from src.db import init_db

def run_pipeline():
    print("Running pipeline...")
    
    records = extract_all()
    events = parse_all(records)

    for event in events:
        load_clean(event)
    print(f"Pipeline finished. Loaded {len(events)} outage events.")

if __name__ == "__main__":
    init_db()
    run_pipeline()
    schedule.every(6).hours.do(run_pipeline)

    while True:
        schedule.run_pending()
        time.sleep(60)