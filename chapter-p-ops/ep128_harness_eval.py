"""EP128 · Evaluating a harness: same fake model, different harness, different score."""
import random


def fake_model(task, tools, rng):
    # Success needs the right tool; otherwise a small lucky chance.
    return task["needs"] in tools or rng.random() < 0.1


def pass_rate(tools, tasks, runs=20, seed=0):
    rng = random.Random(seed)
    ok = sum(fake_model(t, tools, rng) for t in tasks for _ in range(runs))
    return ok / (len(tasks) * runs)


tasks = [{"needs": "read"}, {"needs": "edit"}, {"needs": "shell"}, {"needs": "search"}]
small = {"read", "edit"}
full = {"read", "edit", "shell", "search"}
a, b = pass_rate(small, tasks), pass_rate(full, tasks)
assert b > a
print(f"same model: harness A {a:.0%}, harness B {b:.0%}")
print("harness eval ok")
