# Load Shedding Impact Tracker

A small ETL pipeline that tracks South African load shedding schedules across
several Johannesburg suburbs, using the EskomSePush API. It cleans and stores
outage events in SQLite, then visualizes which areas and stages cause the
most disruption.

## Real-world motivation
Load shedding scheduling is inconsistent and hard to track by memory. This
pipeline builds a historical record so patterns (worst times of day, worst
stages, worst-hit areas) can actually be analyzed instead of guessed at.

## Architecture
Extract (EskomSePush API) → Transform (validate + compute duration) →
Load (SQLite: raw_loadshedding + outage_events) → Analysis (pandas/matplotlib)

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your EskomSePush token
3. `python -m src.main`

## Testing
`pytest tests/`

## Analysis
`python -m analysis.visualize`