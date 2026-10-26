"""EP024 · Context budget. Everything shares one window; reserve room for the reply."""

WINDOW = 8000  # illustrative window size, in tokens


def budget(parts, reserve):
    used = sum(parts.values())
    return {"used": used, "free_for_history": WINDOW - reserve - used, "ok": used + reserve <= WINDOW}


if __name__ == "__main__":
    fixed = {"system": 600, "tools": 1500}  # token counts are illustrative
    print(budget({**fixed, "history": 2000, "tool_results": 3000}, reserve=1000))
    print(budget({**fixed, "history": 2000, "tool_results": 4500}, reserve=1000))  # over budget
