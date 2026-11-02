"""EP088 · Permissions and sandboxing: policy decides allow/deny/ask; code runs with restricted builtins."""

POLICY = {"read_file": "allow", "run_code": "ask", "delete_file": "deny"}


def decide(tool, approve=lambda tool: False):
    mode = POLICY.get(tool, "deny")  # default deny
    if mode == "ask":
        return "allow" if approve(tool) else "deny"
    return mode


def run_sandboxed(code):
    # toy sandbox: no builtins, so open/__import__ are unavailable (not a real security boundary)
    env = {"__builtins__": {}}
    try:
        exec(code, env)
        return env.get("result")
    except Exception as e:
        return f"sandbox error: {type(e).__name__}"


if __name__ == "__main__":
    for t in ("read_file", "run_code", "delete_file", "unknown"):
        print(t, "->", decide(t))
    print(run_sandboxed("result = 2 + 2"))
    print(run_sandboxed("result = open('/etc/hosts').read()"))
