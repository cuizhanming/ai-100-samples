"""EP157 · Audit logs: record tool calls with a timestamp and redact secrets."""
import json, re, time

def redact(text):
    return re.sub(r"(api[_-]?key|token)=\S+", r"\1=[REDACTED]", text, flags=re.I)

def record(log, tool, args, ok):
    log.append({"ts": time.time(), "tool": tool, "args": redact(args), "ok": ok})

log = []
record(log, "bash", "curl -H token=abc123 https://example.com", True)
record(log, "edit", "app.py", True)
assert "abc123" not in json.dumps(log) and "[REDACTED]" in log[0]["args"]
assert [e["tool"] for e in log] == ["bash", "edit"] and all("ts" in e for e in log)
print("audit log ok")
