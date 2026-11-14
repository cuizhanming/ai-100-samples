"""EP147 · Telemetry: emit events, then aggregate them."""
from collections import Counter

events = []


def emit(kind, **meta):
    events.append({"kind": kind, **meta})


emit("turn", tokens=900)
emit("tool", name="read", ok=True)
emit("tool", name="edit", ok=False)
emit("turn", tokens=1200)

assert sum(e["tokens"] for e in events if e["kind"] == "turn") == 2100
assert Counter(e["ok"] for e in events if e["kind"] == "tool")[False] == 1
print("telemetry ok")
