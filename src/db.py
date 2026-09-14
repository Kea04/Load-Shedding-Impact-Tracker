import sqlite3
from config.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_loadshedding (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            area TEXT,
            fetched_at TEXT,
            raw_json TEXT
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS outage_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        area TEXT,
        stage INTEGER,
        start_time TEXT,
        end_time TEXT,
        duration_hours REAL,
        UNIQUE(area, start_time)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized")