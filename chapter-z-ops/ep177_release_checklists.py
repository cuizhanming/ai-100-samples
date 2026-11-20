"""EP177 · Release checklists: ship only when every step is checked."""
checklist = {"evals": True, "tests": True, "diff reviewed": True, "rollback ready": False}

def ready(c):
    return [k for k, v in c.items() if not v]

assert ready(checklist) == ["rollback ready"]
checklist["rollback ready"] = True
assert ready(checklist) == []
print("release checklist ok")
