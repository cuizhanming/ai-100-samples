"""EP176 · Sub-agent limits: refuse spawns beyond a count and depth cap."""
def can_spawn(active, depth, max_active=3, max_depth=2):
    return active < max_active and depth < max_depth

assert can_spawn(2, 1) and not can_spawn(3, 1) and not can_spawn(0, 2)
print("subagent limits ok")
