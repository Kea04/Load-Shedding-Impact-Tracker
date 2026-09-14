from datetime import datetime

def parse_datetime(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None

def parse_area_schedule(area_name, raw_json):
    if not raw_json or "events" not in raw_json:
        return []

    parsed = []
    for event in raw_json.get("events", []):
        start = parse_datetime(event.get("start"))
        end = parse_datetime(event.get("end"))

        if not start or not end:
            continue

        duration_hours = round((end - start).total_seconds() / 3600, 2)
        note = event.get("note", "")
        stage = "".join(filter(str.isdigit, note)) or "0"

        parsed.append({
            "area": area_name,
            "stage": int(stage),
            "start": start.isoformat(),
            "end": end.isoformat(),
            "duration_hours": duration_hours
        })
    return parsed

def parse_all(records):
    all_events = []
    for area_name, raw_json in records.get("areas", {}).items():
        all_events.extend(parse_area_schedule(area_name, raw_json))
    return all_events