"""EP061 · Memory retrieval: score by relevance and recency, inject only the top few."""
import math

MEMORIES = [
    {"text": "prefers short answers", "age_days": 30},
    {"text": "deploys on a mac mini", "age_days": 2},
    {"text": "likes tea", "age_days": 1},
    {"text": "writes short blog posts on agents", "age_days": 5},
]


def score(query, mem):
    overlap = len(set(query.lower().split()) & set(mem["text"].lower().split()))
    return overlap + math.exp(-mem["age_days"] / 14)  # recency decay


def retrieve(query, k=2):
    return sorted(MEMORIES, key=lambda m: score(query, m), reverse=True)[:k]


if __name__ == "__main__":
    for m in retrieve("write a short post about agents"):
        print(round(score("write a short post about agents", m), 2), m["text"])
