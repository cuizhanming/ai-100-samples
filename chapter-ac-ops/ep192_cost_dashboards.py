"""EP192 · Cost dashboards: tally tokens per call and estimate cost (illustrative prices)."""
PRICE_PER_1K = {"in": 0.003, "out": 0.015}  # illustrative, not real pricing
calls = [("read", 2000, 100), ("edit", 3000, 500), ("test", 1000, 50)]

def cost(i, o):
    return i / 1000 * PRICE_PER_1K["in"] + o / 1000 * PRICE_PER_1K["out"]

per = {name: round(cost(i, o), 4) for name, i, o in calls}
total = round(sum(per.values()), 4)
assert max(per, key=per.get) == "edit"
assert total > 0
print("cost dashboards ok:", per, total)
