"""EP141 · IDE integration: the editor is a front end that adds context to the same loop."""


def harness(prompt, context=None):
    context = context or {}
    return f"edit {context.get('file', 'unknown file')} for: {prompt}"


terminal = harness("fix the bug")
ide = harness("fix the bug", {"file": "app.py", "selection": "lines 10-20"})
assert "unknown file" in terminal and "app.py" in ide
print(terminal)
print(ide)
print("ide ok")
