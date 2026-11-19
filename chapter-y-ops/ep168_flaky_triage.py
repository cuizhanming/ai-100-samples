"""EP168 · Flaky-task triage: rerun a task and report the pass rate."""
import random

def pass_rate(task, runs=5):
    return sum(task() for _ in range(runs)) / runs

random.seed(1)
flaky = lambda: random.random() > 0.3
rate = pass_rate(flaky, 20)
assert 0 < rate < 1
print(f"flaky task pass rate {rate:.0%} ok")
