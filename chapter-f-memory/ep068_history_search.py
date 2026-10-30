"""EP068 · Session history search: index past turns and recall a short excerpt."""
HISTORY = [
    {"session": "s1", "date": "2026-10-20", "text": "We chose SQLite for the memory store because it needs no server."},
    {"session": "s2", "date": "2026-10-25", "text": "User asked for weekly summaries on Monday morning."},
    {"session": "s3", "date": "2026-10-28", "text": "Decided to rotate API keys every 90 days."},
]


def search(query, k=1, width=60):
    q = set(query.lower().split())
    hits = sorted(HISTORY, key=lambda h: -len(q & set(h["text"].lower().split())))[:k]
    return [{"session": h["session"], "date": h["date"], "excerpt": h["text"][:width]} for h in hits]


if __name__ == "__main__":
    print(search("which database did we choose"))
