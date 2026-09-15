import random
from datetime import datetime, timedelta

def generate_mock_events(area_name, num_events=5, start_date=None):
    """Generate realistic-looking mock outage events for one area."""
    if start_date is None:
        start_date = datetime.now() - timedelta(days=7)

    events = []
    current = start_date

    for _ in range(num_events):
        # Random gap between outages (6-30 hours apart)
        current += timedelta(hours=random.randint(6, 30))

        stage = random.choice([2, 3, 4, 6])
        duration = {2: 2, 3: 2, 4: 2.5, 6: 4}[stage]  # roughly realistic durations

        start = current
        end = current + timedelta(hours=duration)

        events.append({
            "area": area_name,
            "stage": stage,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "duration_hours": duration
        })

        current = end

    return events

def generate_mock_dataset(areas):
    """Generate mock events across multiple areas."""
    all_events = []
    for area_name in areas:
        all_events.extend(generate_mock_events(area_name))
    return all_events

if __name__ == "__main__":
    from config.config import AREAS
    mock_events = generate_mock_dataset(AREAS.keys())
    for event in mock_events:
        print(event)