"""EP153 · Prompt versioning: keep prompt versions and pick the one that passes more tasks."""
PROMPTS = {"v1": "Fix the bug.", "v2": "Fix the bug. Run the tests and show the diff."}
TASKS = [("t1", "tests"), ("t2", "tests"), ("t3", "diff")]

def fake_agent(prompt, task):
    needs = task[1]
    return {"tests": "tests" in prompt, "diff": "diff" in prompt}[needs]

def score(version):
    return sum(fake_agent(PROMPTS[version], t) for t in TASKS)

scores = {v: score(v) for v in PROMPTS}
best = max(scores, key=scores.get)
assert scores == {"v1": 0, "v2": 3} and best == "v2"
print("prompt versions ok", scores)
