"""EP193 · Tool result truncation: keep head and tail of long output, note what was cut."""
def truncate(text, limit=40):
    if len(text) <= limit:
        return text
    half = limit // 2
    cut = len(text) - limit
    return text[:half] + f"\n[... {cut} chars truncated ...]\n" + text[-half:]

out = "line\n" * 100
short = truncate(out)
assert "truncated" in short
assert len(short) < len(out)
assert truncate("ok") == "ok"
print("tool result truncation ok:", len(out), "->", len(short))
