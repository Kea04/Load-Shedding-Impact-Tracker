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

def plot_stage_frequency(df):
    stage_counts = df["stage"].value_counts().sort_index()
    stage_counts.plot(kind="bar", color="crimson")

    plt.title("Frequency of Each Load Shedding Stage")
    plt.xlabel("Stage")
    plt.ylabel("Number of Outage Events")
    plt.tight_layout()
    plt.savefig("screenshots/stage_frequency.png")

    plt.show()

def plot_hourly_pattern(df):
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["hour"] = df["start_time"].dt.hour

    hourly = df.groupby("hour").size()
    hourly.plot(kind="line", marker="o", color="teal")

    plt.title("Load Shedding Events by Hour of Day")
    plt.xlabel("Hour")
    plt.ylabel("Number of Events")
    plt.tight_layout()
    plt.savefig("screenshots/hourly_pattern.png")

    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_total_hours_by_area(df)
    plot_stage_frequency(df)
    plot_hourly_pattern(df)