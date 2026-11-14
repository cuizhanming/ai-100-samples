"""EP145 · Long-running agents: progress lives in a notes file, so a new session can resume."""
import json, os, tempfile

path = os.path.join(tempfile.mkdtemp(), "progress.json")
STEPS = ["plan", "edit", "test", "ship"]


def run(limit):
    state = json.load(open(path)) if os.path.exists(path) else {"done": []}
    for s in STEPS:
        if s in state["done"] or limit == 0:
            continue
        state["done"].append(s)
        limit -= 1
        json.dump(state, open(path, "w"))
    return state["done"]


assert run(2) == ["plan", "edit"]
assert run(5) == STEPS  # second session resumes from disk
print("long run ok")
