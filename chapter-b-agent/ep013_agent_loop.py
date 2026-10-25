"""EP013 · The agent loop. Observe, think, act, repeat, with a stop rule."""


def think(observation):
    """Toy policy: keep halving until the value is below 1."""
    return "stop" if observation < 1 else "halve"


def run(value, max_steps=20):
    for step in range(1, max_steps + 1):
        action = think(value)  # observe + think
        print(f"step {step}: observe={value:.3f} -> {action}")
        if action == "stop":
            return value
        value /= 2  # act, and the result is the next observation
    print("stopped: max steps")
    return value


if __name__ == "__main__":
    run(10)
