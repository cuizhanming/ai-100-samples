"""EP185 · Headless CI runs: no human, so permissions are fixed up front and failure is an exit code."""
import json

def run_headless(prompt, allow):
    action = "edit" if "fix" in prompt else "deploy"
    ok = action in allow
    return {"output": f"{action} {'done' if ok else 'denied'}", "exit_code": 0 if ok else 1}

r = run_headless("fix the typo", allow={"edit"})
assert r["exit_code"] == 0
assert run_headless("ship it", allow={"edit"})["exit_code"] == 1
print("headless ok:", json.dumps(r))
