"""EP152 · Structured output: validate model JSON against a schema, retry once on error."""
import json

SCHEMA = {"title": str, "score": int}

def validate(text):
    data = json.loads(text)
    for key, typ in SCHEMA.items():
        if not isinstance(data.get(key), typ):
            raise ValueError(f"bad field: {key}")
    return data

replies = iter(['{"title": "ok", "score": "high"}', '{"title": "ok", "score": 7}'])
try:
    data = validate(next(replies))
except ValueError:
    data = validate(next(replies))  # send the error back, retry once
assert data == {"title": "ok", "score": 7}
print("structured ok")
