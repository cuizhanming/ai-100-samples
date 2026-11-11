"""EP131 · Plan mode: read-only tools until the plan is approved; todo list as state."""
READ_ONLY = {"read", "search"}
ALL = READ_ONLY | {"edit", "shell"}


def run(steps, approved):
    allowed = ALL if approved else READ_ONLY
    todo = [{"task": s["task"], "done": False} for s in steps]
    for item, s in zip(todo, steps):
        if s["tool"] in allowed:
            item["done"] = True
    return todo


steps = [{"task": "find the bug", "tool": "search"}, {"task": "fix it", "tool": "edit"}]
before, after = run(steps, False), run(steps, True)
assert [t["done"] for t in before] == [True, False]
assert all(t["done"] for t in after)
print("plan mode blocked edit until approval; todo:", after)
print("plan mode ok")
