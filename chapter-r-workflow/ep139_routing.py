"""EP139 · Model routing: easy steps go to a small model, hard ones to the large model."""
PRICE = {"small": 1, "large": 10}  # illustrative relative cost per step


def route(step):
    return "small" if step in {"title", "summary"} else "large"


steps = ["title", "summary", "refactor", "title"]
plan = [route(s) for s in steps]
routed = sum(PRICE[m] for m in plan)
all_large = PRICE["large"] * len(steps)
assert plan == ["small", "small", "large", "small"] and routed < all_large
print(plan, f"cost {routed} vs {all_large} (illustrative)")
print("routing ok")
