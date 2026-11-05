"""EP109 · Compaction: when history nears the limit, replace old turns with a (lossy) summary."""


def tokens(msgs):
    return sum(len(m) // 4 + 1 for m in msgs)  # crude, illustrative


def compact(history, limit, keep_last=2, summarise=lambda old: "SUMMARY of %d earlier turns" % len(old)):
    if tokens(history) <= limit:
        return history
    old, recent = history[:-keep_last], history[-keep_last:]
    return [summarise(old)] + recent  # detail in `old` is gone


history = ["turn %d: %s" % (i, "x" * 80) for i in range(20)]
print("before:", tokens(history), "tokens,", len(history), "messages")
history = compact(history, limit=200)
print("after: ", tokens(history), "tokens,", len(history), "messages ->", history[0])
