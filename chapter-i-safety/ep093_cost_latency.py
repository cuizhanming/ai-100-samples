"""EP093 · Cost and latency control: a turn cap, a token budget and cheap-model routing (illustrative prices)."""

PRICE_PER_1K = {"small": 0.1, "large": 1.0}  # illustrative units
MAX_TURNS, MAX_COST = 6, 2.0


def pick_model(task):
    return "small" if len(task) < 40 else "large"


def run(task):
    cost = 0.0
    for turn in range(1, MAX_TURNS + 1):
        model = pick_model(task)
        cost += 0.8 * PRICE_PER_1K[model]  # pretend each turn uses 800 tokens
        if cost > MAX_COST:
            return f"stopped at turn {turn}: budget {MAX_COST} exceeded (cost {cost:.2f})"
    return f"stopped at max turns, cost {cost:.2f}"


if __name__ == "__main__":
    print("short:", run("rename a file"))
    print("long: ", run("refactor the whole billing module and update every test"))
