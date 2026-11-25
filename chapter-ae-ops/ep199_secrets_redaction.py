"""EP199 · Secrets redaction: mask key-like tokens before text reaches logs or the model."""
import re

PATTERN = re.compile(r"(sk|ghp|key)[-_][A-Za-z0-9]{8,}")

def redact(text):
    return PATTERN.sub("[REDACTED]", text)

out = redact("export API=sk-abc12345XYZ and token ghp_0123456789abcd")
assert "sk-abc" not in out and "ghp_0123" not in out
assert out.count("[REDACTED]") == 2
print("secrets redaction ok:", out)
