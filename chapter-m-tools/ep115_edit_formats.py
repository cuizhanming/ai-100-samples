"""EP115 · Edit formats: whole-file rewrite vs exact replace vs unified diff."""
import difflib

old = "".join(f"line {i}\n" for i in range(1, 21))
new = old.replace("line 7\n", "line seven\n")


def replace_edit(text, o, n):
    if text.count(o) != 1:
        raise ValueError("old text must match exactly once")
    return text.replace(o, n)


diff = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), "a", "b", n=1))
assert replace_edit(old, "line 7\n", "line seven\n") == new
print(f"whole file: {len(new)} chars | replace: {len('line 7line seven')} chars | diff: {len(diff)} chars")
print(diff)
