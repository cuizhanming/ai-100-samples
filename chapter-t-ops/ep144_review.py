"""EP144 · Review agents: a reviewer sees only the diff and flags risky lines."""
DIFF = ["+ password = 'hunter2'", "+ total = a + b", "+ # TODO remove"]
RULES = {"hard-coded secret": "password =", "leftover TODO": "TODO"}


def review(diff):
    return [name for line in diff for name, pat in RULES.items() if pat in line]


found = review(DIFF)
assert found == ["hard-coded secret", "leftover TODO"]
print("review ok", found)
