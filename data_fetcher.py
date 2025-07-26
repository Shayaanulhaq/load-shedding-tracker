import json
import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("schedule_data.json")


def get_today_slots(feeder_code: str = "IESCO-1") -> dict:
    """Return today's outage slots for the given feeder from the local JSON."""
    today = datetime.date.today().strftime("%Y-%m-%d")

    try:
        data = json.loads(DATA_FILE.read_text())
        slots = data.get(feeder_code.upper(), [])
    except (FileNotFoundError, json.JSONDecodeError):
        slots = []

    return {"date": today, "slots": slots}


if __name__ == "__main__":
    print(get_today_slots())

