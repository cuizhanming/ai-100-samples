"""EP167 · Data retention: expire old transcripts, keep only audit-tagged ones."""

def sweep(files, today, max_age=30):
    return [f["name"] for f in files if today - f["day"] > max_age and not f.get("audit")]

files = [{"name": "a", "day": 1}, {"name": "b", "day": 90, "audit": True}, {"name": "c", "day": 100}]
assert sweep(files, 100) == ["a"]
print("data retention ok")
