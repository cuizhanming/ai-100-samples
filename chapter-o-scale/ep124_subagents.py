"""EP124 · Subagents: heavy work happens in a separate context; only a summary returns."""
def subagent(task, files):
    context = [f"read {f}" for f in files]  # stays inside the subagent
    return f"{task}: {len(context)} files, 1 finding"


main_context = ["user goal"]
main_context.append(subagent("audit", ["a.py", "b.py", "c.py"]))
assert len(main_context) == 2
print(main_context)
