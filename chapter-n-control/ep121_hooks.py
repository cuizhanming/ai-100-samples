"""EP121 · Hooks: pre-hooks can block a tool call, post-hooks observe the result."""
def pre_hook(tool, args):
    if tool == "shell" and "rm -rf" in args:
        return "block"
    return "ok"


def post_hook(tool, result, log):
    log.append((tool, len(result)))


def run_tool(tool, args, log):
    if pre_hook(tool, args) == "block":
        return "blocked by hook"
    result = f"ran {tool}({args})"
    post_hook(tool, result, log)
    return result


log = []
assert run_tool("shell", "rm -rf /", log) == "blocked by hook"
assert run_tool("shell", "ls", log).startswith("ran")
assert len(log) == 1
print(log)
