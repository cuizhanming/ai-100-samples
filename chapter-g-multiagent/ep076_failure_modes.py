"""EP076 · Coordination failure modes: a ping-pong loop stopped by a turn cap."""


def a(x):
    return "b", x + 1


def b(x):
    return "a", x + 1  # never finishes: bounces forever without a guard


def run(max_turns=6):
    who, x = "a", 0
    for turn in range(max_turns):
        who, x = (a if who == "a" else b)(x)
    return f"stopped after {max_turns} turns (guard), still unfinished"


if __name__ == "__main__":
    print(run())
