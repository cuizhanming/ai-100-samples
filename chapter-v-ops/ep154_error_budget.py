"""EP154 · Error budgets: compare a measured failure rate with a target."""
def within_budget(results, budget=0.10):
    failures = sum(1 for r in results if not r)
    rate = failures / len(results)
    return rate <= budget, rate

ok, rate = within_budget([True] * 19 + [False])
assert ok and rate == 0.05
ok, rate = within_budget([True] * 7 + [False] * 3)
assert not ok and rate == 0.3
print("error budget ok")
