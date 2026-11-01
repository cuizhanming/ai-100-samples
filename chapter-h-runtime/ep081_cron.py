"""EP081 · Cron and scheduling: exact-time jobs, each in its own isolated run."""
from datetime import datetime, timedelta, timezone

JOBS = [
    {"name": "daily-report", "at": "09:00", "tz": "Europe/Dublin"},
    {"name": "one-shot-reminder", "at": datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc), "once": True},
]


def due(job, now):
    if job.get("once"):
        return now >= job["at"]
    return now.strftime("%H:%M") == job["at"]  # simplified: ignores the job's timezone


if __name__ == "__main__":
    now = datetime(2026, 1, 1, 9, 0, tzinfo=timezone.utc)
    for j in JOBS:
        print(j["name"], "due now" if due(j, now) else "not yet")
    print("one-shot due later:", due(JOBS[1], now + timedelta(hours=3)))
