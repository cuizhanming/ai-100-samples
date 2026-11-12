"""EP135 · Headless mode: prompt in, output and exit code out, with tools pre-approved."""
import json
import sys

ALLOWED = {"read", "test"}


def run_headless(prompt, tool_calls):
    out = []
    for t in tool_calls:
        if t not in ALLOWED:
            return {"output": out, "error": f"tool '{t}' needs approval", "exit": 1}
        out.append(t)
    return {"output": out, "error": None, "exit": 0}


ok = run_headless("fix tests", ["read", "test"])
stalled = run_headless("fix tests", ["read", "shell"])
assert ok["exit"] == 0 and stalled["exit"] == 1
print(json.dumps(ok))
print("headless ok")
sys.exit(0)
