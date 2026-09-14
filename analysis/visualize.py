import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from config.config import DB_PATH

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM outage_events", conn)
    conn.close()
    return df

def plot_total_hours_by_area(df):
    totals = df.groupby("area")["duration_hours"].sum().sort_values()

    totals.plot(kind="barh", color="darkorange")
    plt.title("Total Load Shedding Hours by Area")
    plt.xlabel("Hours")
    plt.tight_layout()
    plt.savefig("screenshots/total_hours_by_area.png")
    
    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_total_hours_by_area(df)