"""EP178 · Hooks: run your code at lifecycle events, and let it block a step."""
hooks = {}

def on(event):
    def reg(fn):
        hooks.setdefault(event, []).append(fn)
        return fn
    return reg

@on("before_tool")
def block_rm(call):
    return "rm -rf" not in call["cmd"]

def fire(event, call):
    return all(h(call) for h in hooks.get(event, []))

assert fire("before_tool", {"cmd": "ls"}) is True
assert fire("before_tool", {"cmd": "rm -rf /"}) is False
print("hooks ok")
