"""EP091 · Evals for agents: a fixed task set, repeated runs, and a pass rate you can track."""
import random

TASKS = [("2+3", "5"), ("10-4", "6"), ("3*3", "9")]


def toy_agent(task, rng):
    ans = str(eval(task))  # fine for trusted toy inputs only
    return ans if rng.random() > 0.3 else "?"  # 30% simulated flakiness


def evaluate(runs=5, seed=0):
    rng = random.Random(seed)
    passed = sum(toy_agent(t, rng) == want for t, want in TASKS for _ in range(runs))
    total = len(TASKS) * runs
    return passed, total


if __name__ == "__main__":
    p, n = evaluate()
    print(f"pass rate {p}/{n} = {p / n:.0%}")
