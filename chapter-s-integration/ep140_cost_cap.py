"""EP140 · Cost caps: stop the loop when spend or turns exceed a budget."""
COST_PER_TURN = 3  # illustrative units


def run(max_cost, max_turns, needed_turns):
    spent = turns = 0
    while turns < needed_turns:
        if spent + COST_PER_TURN > max_cost or turns >= max_turns:
            return turns, spent, "stopped"
        spent += COST_PER_TURN
        turns += 1
    return turns, spent, "done"


assert run(100, 10, 5) == (5, 15, "done")
assert run(10, 50, 20) == (3, 9, "stopped")
assert run(100, 4, 20)[2] == "stopped"
print("cost cap ok")
