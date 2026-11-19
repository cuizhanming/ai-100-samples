"""EP169 · Approval fatigue: allow safe commands, ask on risky ones, deny dangerous ones."""
ALLOW, DENY = {"ls", "git status", "pytest"}, {"rm -rf /"}

def decide(cmd):
    if cmd in DENY:
        return "deny"
    return "allow" if cmd in ALLOW else "ask"

assert [decide(c) for c in ("ls", "git push", "rm -rf /")] == ["allow", "ask", "deny"]
print("approval rules ok")
