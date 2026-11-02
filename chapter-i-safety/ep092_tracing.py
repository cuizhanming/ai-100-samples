"""EP092 · Tracing and logging: one trace per run, a span per step, secrets redacted."""
import re
import time
import uuid


class Trace:
    def __init__(self):
        self.id = uuid.uuid4().hex[:8]
        self.spans = []

    def span(self, name, **data):
        clean = {k: re.sub(r"sk-\w+", "sk-***", str(v)) for k, v in data.items()}
        self.spans.append({"name": name, "t": round(time.time(), 3), **clean})


if __name__ == "__main__":
    tr = Trace()
    tr.span("model_call", tokens=120, prompt="use key sk-abc123")
    tr.span("tool_call", tool="search", ok=True)
    tr.span("model_call", tokens=80)
    print("trace", tr.id, "with", len(tr.spans), "spans")
    for s in tr.spans:
        print(s["name"], {k: v for k, v in s.items() if k not in ("name", "t")})
