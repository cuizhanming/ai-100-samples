"""EP165 · Change windows: allow config changes only inside a quiet window, one at a time."""
from datetime import datetime

WINDOW = (2, 5)  # 02:00-05:00 local

def may_change(now, pending):
    return WINDOW[0] <= now.hour < WINDOW[1] and pending == 0

assert may_change(datetime(2026, 1, 1, 3, 0), 0)
assert not may_change(datetime(2026, 1, 1, 14, 0), 0)
assert not may_change(datetime(2026, 1, 1, 3, 0), 1)
print("change window ok")
