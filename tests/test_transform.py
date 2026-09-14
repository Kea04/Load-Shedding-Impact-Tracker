from src.transform import parse_area_schedule

def test_parse_area_schedule_valid():
    raw = {
        "events": [
            {"start": "2026-09-12T18:00:00+02:00",
             "end": "2026-09-12T20:30:00+02:00",
             "note": "Stage 4"}
        ]
    }
    result = parse_area_schedule("Sandton", raw)
    assert len(result) == 1
    assert result[0]["stage"] == 4
    assert result[0]["duration_hours"] == 2.5

def test_parse_area_schedule_missing_events():
    assert parse_area_schedule("Soweto", {}) == []

def test_parse_area_schedule_bad_dates():
    raw = {"events": [{"start": None, "end": None, "note": "Stage 2"}]}
    assert parse_area_schedule("Randburg", raw) == []