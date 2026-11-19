"""EP172 · Policy as code: diff two policy versions like a code review."""
old = {"allow": ["ls"], "deny": ["rm -rf /"]}
new = {"allow": ["ls", "pytest"], "deny": ["rm -rf /"]}

def diff(a, b):
    return {k: sorted(set(b[k]) ^ set(a[k])) for k in a if set(a[k]) != set(b[k])}

assert diff(old, new) == {"allow": ["pytest"]}
print("policy diff ok")
