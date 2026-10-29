"""EP053 · Checkpoints and resume. Save state after each step; a crash resumes mid-run."""
import json
import os
import tempfile

STEPS = ["fetch", "parse", "store", "notify"]


def run(path, crash_at=None):
    state = json.load(open(path)) if os.path.exists(path) else {"done": []}
    for step in STEPS:
        if step in state["done"]:
            continue
        if step == crash_at:
            raise RuntimeError(f"crashed during {step}")
        state["done"].append(step)
        json.dump(state, open(path, "w"))
    return state["done"]


if __name__ == "__main__":
    path = os.path.join(tempfile.mkdtemp(), "thread-1.json")
    try:
        run(path, crash_at="store")
    except RuntimeError as err:
        print(err)
    print("resumed:", run(path))
