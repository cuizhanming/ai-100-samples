"""EP170 · Prompt caching: only a stable prefix can be reused."""

def cached_tokens(prev, cur):
    n = 0
    for a, b in zip(prev, cur):
        if a != b:
            break
        n += 1
    return n

system, tools = ["sys"] * 50, ["tool"] * 30
turn1 = system + tools + ["u1"]
turn2 = system + tools + ["u1", "a1", "u2"]
edited = ["SYS2"] + system[1:] + tools + ["u1"]
assert cached_tokens(turn1, turn2) == 81
assert cached_tokens(turn1, edited) == 0
print("prompt caching ok")
