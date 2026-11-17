"""EP159 · Incident replay: rebuild what happened from a saved event log."""
import json

log = [
    {"step": 1, "tool": "read", "arg": "config.yml", "ok": True},
    {"step": 2, "tool": "bash", "arg": "rm -rf build", "ok": True},
    {"step": 3, "tool": "bash", "arg": "deploy.sh", "ok": False},
]

def replay(events):
    return [f"{e['step']}: {e['tool']} {e['arg']} -> {'ok' if e['ok'] else 'FAILED'}" for e in events]

def first_failure(events):
    return next((e for e in events if not e["ok"]), None)

saved = json.loads(json.dumps(log))
assert replay(saved)[2].endswith("FAILED")
assert first_failure(saved)["step"] == 3
print("incident replay ok")
