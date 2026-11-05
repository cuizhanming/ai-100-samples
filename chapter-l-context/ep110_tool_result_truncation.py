"""EP110 · Tool-result truncation: cap big outputs, keep head and tail, say what was cut."""


def truncate(output, max_chars=200):
    if len(output) <= max_chars:
        return output
    half = max_chars // 2
    cut = len(output) - max_chars
    return output[:half] + f"\n...[{cut} chars truncated; re-run with a narrower range]...\n" + output[-half:]


big = "\n".join(f"line {i}" for i in range(500))
small = truncate(big)
print(f"original {len(big)} chars -> sent {len(small)} chars")
print(small)
