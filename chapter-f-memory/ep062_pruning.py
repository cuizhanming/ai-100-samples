"""EP062 · Pruning and dreaming: a scheduled pass merges duplicates and archives stale notes."""


def dream(memories, today, max_age=90):
    keep, archive, seen = [], [], {}
    for m in sorted(memories, key=lambda m: m["date"]):
        key = m["text"].lower()
        if key in seen:  # newer duplicate refreshes the date
            seen[key]["date"] = m["date"]
            continue
        seen[key] = dict(m)
    for m in seen.values():
        age = (today - m["date"]) if isinstance(m["date"], int) else 0
        (archive if age > max_age else keep).append(m)
    return keep, archive


if __name__ == "__main__":
    # dates are day numbers for simplicity
    mems = [
        {"text": "Uses Bun", "date": 10},
        {"text": "uses bun", "date": 200},
        {"text": "Old project X", "date": 20},
        {"text": "Prefers short answers", "date": 190},
    ]
    keep, archive = dream(mems, today=210)
    print("keep:", keep)
    print("archive:", archive)
