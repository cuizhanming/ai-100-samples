"""EP189 · Permission allowlists: pre-approve exact commands; everything else asks."""
ALLOW = {"git status", "pytest -q"}

def decide(cmd):
    return "allow" if cmd in ALLOW else "ask"

assert decide("git status") == "allow"
assert decide("git push --force") == "ask"
assert decide("pytest -q; rm -rf /") == "ask"  # exact match, no wildcard leak
print("permission allowlists ok")
