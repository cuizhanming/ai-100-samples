"""EP166 · On-call for agents: route alerts on error rate, cost or loops to a named owner."""

OWNERS = {"errors": "alice", "cost": "bob", "loop": "alice"}

def alerts(m):
    out = []
    if m["error_rate"] > 0.2: out.append("errors")
    if m["cost_usd"] > 50: out.append("cost")
    if m["repeat_calls"] > 10: out.append("loop")
    return [(a, OWNERS[a]) for a in out]

assert alerts({"error_rate": 0.0, "cost_usd": 3, "repeat_calls": 1}) == []
assert alerts({"error_rate": 0.5, "cost_usd": 80, "repeat_calls": 2}) == [("errors", "alice"), ("cost", "bob")]
assert alerts({"error_rate": 0, "cost_usd": 1, "repeat_calls": 30}) == [("loop", "alice")]
print("on-call ok")
