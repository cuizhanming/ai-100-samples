"""EP112 · Hidden model calls: a session log shows main-loop calls and side calls. Illustrative data."""
calls = [
    ("main", "user prompt", 4200),
    ("side", "session title", 300),
    ("main", "tool result follow-up", 4800),
    ("side", "summary for compaction", 1500),
    ("main", "final answer", 5100),
]
total = sum(t for _, _, t in calls)
side = sum(t for k, _, t in calls if k == "side")
for kind, why, tokens in calls:
    print(f"{kind:4} {why:24} {tokens:5} tokens")
print(f"side calls: {side}/{total} tokens ({side / total:.0%})")
