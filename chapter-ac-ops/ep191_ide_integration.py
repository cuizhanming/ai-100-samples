"""EP191 · IDE integration: editor state becomes context; edits return as diffs."""
editor = {"file": "app.py", "selection": "def f(): pass", "errors": ["E1: unused"]}

def context_from_editor(e):
    return [f"file={e['file']}", f"selection={e['selection']}", *e["errors"]]

def as_diff(old, new):
    return [f"-{old}", f"+{new}"]

ctx = context_from_editor(editor)
diff = as_diff("def f(): pass", "def f(): return 1")
assert len(ctx) == 3
assert diff[0].startswith("-") and diff[1].startswith("+")
print("ide integration ok")
