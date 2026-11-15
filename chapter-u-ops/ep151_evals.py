"""EP151 · Evals for your tasks: a tiny pass/fail suite compared across two settings."""
tasks = [("add", lambda f: f(2, 3) == 5), ("neg", lambda f: f(-1, 1) == 0)]

def run(agent):
    return sum(check(agent) for _, check in tasks) / len(tasks)

good = lambda a, b: a + b
bad = lambda a, b: a * b
assert run(good) == 1.0
assert run(bad) == 0.0
assert run(good) > run(bad)  # catches the regression
print("evals ok")
