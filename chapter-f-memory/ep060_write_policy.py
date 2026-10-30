"""EP060 · Memory write policy: save durable facts, skip chatter, secrets and duplicates."""
import re

SECRET = re.compile(r"(api[_-]?key|password|token)\s*[:=]", re.I)


def should_write(candidate, store):
    text = candidate["text"].strip()
    if candidate["kind"] == "chatter" or len(text) < 8:
        return False, "not durable"
    if SECRET.search(text):
        return False, "looks like a secret"
    if text.lower() in (x["text"].lower() for x in store):
        return False, "duplicate"
    return True, "ok"


if __name__ == "__main__":
    store = []
    candidates = [
        {"kind": "fact", "text": "User works in the Europe/Dublin timezone"},
        {"kind": "chatter", "text": "haha nice"},
        {"kind": "fact", "text": "api_key = abc123"},
        {"kind": "fact", "text": "user works in the europe/dublin timezone"},
    ]
    for c in candidates:
        ok, why = should_write(c, store)
        if ok:
            store.append({**c, "date": "2026-10-30"})
        print(f"{'WRITE' if ok else 'skip '} ({why}): {c['text']}")
    print("store:", store)
