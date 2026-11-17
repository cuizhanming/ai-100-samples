"""EP158 · Cost attribution: tag each model call with a task and sum cost per task."""
from collections import defaultdict

PRICE_PER_1K = {"in": 0.003, "out": 0.015}  # illustrative prices

def cost(tokens_in, tokens_out):
    return tokens_in / 1000 * PRICE_PER_1K["in"] + tokens_out / 1000 * PRICE_PER_1K["out"]

calls = [("fix-bug", 4000, 500), ("fix-bug", 2000, 300), ("write-docs", 1000, 800)]
per_task = defaultdict(float)
for task, i, o in calls:
    per_task[task] += cost(i, o)
assert round(per_task["fix-bug"], 4) == 0.0285 and round(per_task["write-docs"], 4) == 0.015
assert max(per_task, key=per_task.get) == "fix-bug"
print("cost attribution ok")
