"""EP130 · Build a mini harness: loop + tools + permissions + truncation + turn cap."""
TOOLS = {"echo": lambda a: a, "big": lambda a: "x" * 500, "rm": lambda a: "deleted"}
ALLOWED = {"echo", "big"}
MAX_TURNS, MAX_RESULT = 5, 100


def scripted_model(history):
    steps = [("echo", "hi"), ("rm", "/"), ("big", ""), None]
    n = sum(1 for h in history if h[0] == "assistant")
    return steps[min(n, len(steps) - 1)]


def run(model):
    history = [("user", "do the job")]
    for _ in range(MAX_TURNS):
        req = model(history)
        history.append(("assistant", req))
        if req is None:
            return history
        name, arg = req
        if name not in ALLOWED:
            result = "denied: " + name
        else:
            result = TOOLS[name](arg)[:MAX_RESULT]
        history.append(("tool", result))
    return history


h = run(scripted_model)
tool_results = [x[1] for x in h if x[0] == "tool"]
assert "denied: rm" in tool_results
assert all(len(r) <= MAX_RESULT for r in tool_results)
assert h[-1] == ("assistant", None)
print("mini harness ok:", len(h), "events")
