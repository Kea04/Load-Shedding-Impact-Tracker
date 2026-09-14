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
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized")