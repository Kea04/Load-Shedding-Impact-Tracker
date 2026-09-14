import json
from datetime import datetime
from src.db import get_connection

def load_raw(area, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO raw_loadshedding (area, fetched_at, raw_json) VALUES (?, ?, ?)",
        (area, datetime.now().isoformat(), json.dumps(data))
    )

    conn.commit()
    conn.close()

def load_clean(event):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO outage_events
        (area, stage, start_time, end_time, duration_hours)
        VALUES (?, ?, ?, ?, ?)
    """, (
        event["area"], event["stage"], event["start"],
        event["end"], event["duration_hours"]
    ))
    
    conn.commit()
    conn.close()