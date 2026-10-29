"""EP048 · Stop conditions. Done, blocked, or out of steps: always say why we stopped."""


def agent_step(i):
    return {"done": i == 4, "blocked": False}


def run(max_steps=10):
    for i in range(1, max_steps + 1):
        s = agent_step(i)
        if s["done"]:
            return "done", i
        if s["blocked"]:
            return "blocked", i
    return "limit", max_steps


if __name__ == "__main__":
    reason, steps = run()
    print(f"stopped: {reason} after {steps} steps")
    print("with a cap of 3:", run(max_steps=3))
