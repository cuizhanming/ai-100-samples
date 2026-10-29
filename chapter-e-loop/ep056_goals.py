"""EP056 · Goals and long-running work. A written goal plus progress notes survive restarts."""
import json
import os
import tempfile


def load(path, goal):
    if os.path.exists(path):
        return json.load(open(path))
    return {"goal": goal, "todo": ["research", "draft", "review"], "done": []}


def work(path, goal, max_steps):
    state = load(path, goal)
    for _ in range(max_steps):
        if not state["todo"]:
            break
        state["done"].append(state["todo"].pop(0))
        json.dump(state, open(path, "w"))
    return state


if __name__ == "__main__":
    path = os.path.join(tempfile.mkdtemp(), "goal.json")
    print("session 1:", work(path, "ship the report", 2))
    print("session 2:", work(path, "(ignored)", 5))
