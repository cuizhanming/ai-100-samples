"""EP129 · Cost per task: total spend divided by tasks actually solved."""


def cost_per_solved(runs):
    total = sum(r["cost"] for r in runs)
    solved = sum(r["passed"] for r in runs)
    return float("inf") if solved == 0 else total / solved


cheap = [{"cost": 0.10, "passed": False}] * 7 + [{"cost": 0.10, "passed": True}] * 3
solid = [{"cost": 0.25, "passed": True}] * 9 + [{"cost": 0.25, "passed": False}]
a, b = cost_per_solved(cheap), cost_per_solved(solid)
assert a > b
print(f"cheap model ${a:.2f}/solve, pricier model ${b:.2f}/solve")
print("cost per task ok")
