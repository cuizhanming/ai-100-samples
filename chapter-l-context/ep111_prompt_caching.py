"""EP111 · Prompt caching: only an unchanged prefix can be reused. Token counts are illustrative."""


def cached_prefix(prev, cur):
    n = 0
    for a, b in zip(prev, cur):
        if a != b:
            break
        n += 1
    return n


turn1 = ["tools", "rules", "history-1", "question-1"]
turn2_good = ["tools", "rules", "history-1", "question-1", "answer-1", "question-2"]
turn2_bad = ["tools", "rules-v2", "history-1", "question-1", "answer-1", "question-2"]
for name, t in (("stable order", turn2_good), ("early change", turn2_bad)):
    print(f"{name}: {cached_prefix(turn1, t)} of {len(t)} blocks reusable")
