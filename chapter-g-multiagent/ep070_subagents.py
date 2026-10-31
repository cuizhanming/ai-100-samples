"""EP070 · Subagents: the child works in a fresh context; only a short result returns."""


def subagent(brief, files):
    context = [brief]  # fresh context: only the brief, not the parent history
    for f in files:
        context.append(f"read {f} ({len(f) * 100} tokens, illustrative)")
    return f"summary of {len(files)} files for: {brief}"


if __name__ == "__main__":
    parent_history = ["user: audit the repo"] * 50
    result = subagent("list TODOs", ["a.py", "b.py", "c.py"])
    parent_history.append(result)
    print(len(parent_history), "parent messages;", result)
