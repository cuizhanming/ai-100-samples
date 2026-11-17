"""EP162 · Sandbox escapes: block paths that resolve outside the allowed root."""
import os

ROOT = "/work/project"

def allowed(path):
    full = os.path.normpath(os.path.join(ROOT, path))
    return full == ROOT or full.startswith(ROOT + os.sep)

assert allowed("src/app.py")
assert not allowed("../secrets.txt")
assert not allowed("src/../../etc/passwd")
assert not allowed("/etc/passwd")
print("sandbox escape ok")
