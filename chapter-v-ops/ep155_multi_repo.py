"""EP155 · Multi-repo work: only paths under allowed roots are visible to the agent."""
from pathlib import PurePosixPath

ROOTS = [PurePosixPath("/work/api"), PurePosixPath("/work/web")]

def allowed(path):
    p = PurePosixPath(path)
    return any(r == p or r in p.parents for r in ROOTS)

assert allowed("/work/api/app.py") and allowed("/work/web/src/index.ts")
assert not allowed("/work/secrets/key.txt") and not allowed("/home/me/.ssh/id")
print("multi-repo scope ok")
