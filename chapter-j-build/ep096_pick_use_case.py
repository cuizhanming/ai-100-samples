"""EP096 · Pick a use case: score candidate tasks by value, frequency and risk, then start with the best one."""

CANDIDATES = [
    {"task": "summarize daily email", "value": 3, "frequency": 5, "risk": 1},
    {"task": "auto-send customer refunds", "value": 5, "frequency": 2, "risk": 5},
    {"task": "triage bug reports", "value": 4, "frequency": 4, "risk": 2},
]


def score(c):
    return c["value"] * c["frequency"] - 3 * c["risk"]  # illustrative weights


if __name__ == "__main__":
    for c in sorted(CANDIDATES, key=score, reverse=True):
        print(f"{score(c):>3}  {c['task']}")
    print("start with:", max(CANDIDATES, key=score)["task"])
