"""EP181 · Diff review: trust the diff, flag deleted tests and unrelated files."""
import difflib

old = ["def add(a, b):", "    return a + b", "", "def test_add():", "    assert add(1, 2) == 3"]
new = ["def add(a, b):", "    return a + b"]
removed = [l for l in difflib.unified_diff(old, new, lineterm="") if l.startswith("-") and not l.startswith("---")]
flag = any("test_" in l or "assert" in l for l in removed)

assert flag is True
print("diff review ok: a test was deleted")
