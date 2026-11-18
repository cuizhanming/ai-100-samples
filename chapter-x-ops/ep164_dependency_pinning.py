"""EP164 · Dependency pinning: fail CI when installed tool versions differ from the pinned ones."""

PINNED = {"harness": "1.4.2", "plugin-lint": "0.9.1"}

def drift(installed):
    return {k: (PINNED[k], v) for k, v in installed.items() if PINNED.get(k) != v}

assert drift({"harness": "1.4.2", "plugin-lint": "0.9.1"}) == {}
assert drift({"harness": "1.5.0", "plugin-lint": "0.9.1"}) == {"harness": ("1.4.2", "1.5.0")}
print("dependency pinning ok")
