"""EP187 · Model switching: choose a model per task; the harness stays the same."""
MODELS = {"small": 1, "large": 10}

def pick(task_hard):
    return "large" if task_hard else "small"

session = [pick(False), pick(True)]
cost = sum(MODELS[m] for m in session)

assert session == ["small", "large"]
assert cost == 11
print("model switching ok: cost", cost)
