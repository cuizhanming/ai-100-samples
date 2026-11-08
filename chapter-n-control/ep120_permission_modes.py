"""EP120 · Permission modes: deny > allow > mode default decides ask/allow."""
MODES = {"plan": {"read"}, "default": {"read"}, "accept_edits": {"read", "edit"}, "bypass": {"read", "edit", "shell"}}
DENY = {("shell", "rm -rf")}


def decide(mode, action, detail=""):
    if any(action == a and d in detail for a, d in DENY):
        return "deny"
    if mode == "plan" and action != "read":
        return "deny"
    return "allow" if action in MODES[mode] else "ask"


assert decide("default", "edit") == "ask"
assert decide("accept_edits", "edit") == "allow"
assert decide("bypass", "shell", "rm -rf /") == "deny"
for m in MODES:
    print(m, [decide(m, a) for a in ("read", "edit", "shell")])
