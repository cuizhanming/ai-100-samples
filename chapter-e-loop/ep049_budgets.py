"""EP049 · Max steps and budgets. Stop cleanly when turns or (illustrative) cost run out."""


def run(max_turns=5, max_cost=0.05, cost_per_turn=0.02):
    spent = 0.0
    for turn in range(1, max_turns + 1):
        if spent + cost_per_turn > max_cost:
            return f"halted before turn {turn}: budget {max_cost:.2f} would be exceeded"
        spent += cost_per_turn
    return f"finished {max_turns} turns, spent {spent:.2f}"


if __name__ == "__main__":
    print(run())
    print(run(max_cost=1.0))
