"""EP173 · Context budgets: trim oldest turns until the window fits with room to reply."""
def trim(turns, window, reserve):
    turns = list(turns)
    while sum(t[1] for t in turns) > window - reserve and len(turns) > 1:
        turns.pop(0)
    return turns

kept = trim([("a", 400), ("b", 300), ("c", 200)], window=800, reserve=200)
assert [t[0] for t in kept] == ["b", "c"]
print("context budget ok")
