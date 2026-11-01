"""EP085 · Local vs cloud: choose by privacy first, then quality and cost (illustrative numbers)."""


def choose(private, hard, budget_per_1k):
    if private:
        return "local"
    if hard:
        return "cloud"
    return "local" if budget_per_1k < 0.001 else "cloud"


if __name__ == "__main__":
    cases = [(True, True, 1.0), (False, True, 1.0), (False, False, 0.0005), (False, False, 0.01)]
    for c in cases:
        print(dict(zip(("private", "hard", "budget_per_1k"), c)), "->", choose(*c))
