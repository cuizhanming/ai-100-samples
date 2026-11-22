"""EP184 · Plan mode: read-only tools are allowed, edits are blocked until approved."""
READ_ONLY = {"read", "grep"}

def allowed(tool, plan_mode, approved):
    return tool in READ_ONLY or not plan_mode or approved

assert allowed("read", True, False)
assert not allowed("edit", True, False)
assert allowed("edit", True, True)
print("plan mode ok: edits wait for approval")
