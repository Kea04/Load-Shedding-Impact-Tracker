def parse_area_schedule(area_name, raw_json):
    events = raw_json.get("events", [])
    parsed = []
    for event in events:
        parsed.append({
            "area": area_name,
            "stage": event.get("note", "").replace("Stage ", ""),
            "start": event.get("start"),
            "end": event.get("end"),
        })
    return parsed