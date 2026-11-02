"""EP089 · Least privilege: each agent gets only the tools its task needs."""

TOOLS = {
    "read_docs": lambda q: f"docs about {q}",
    "write_file": lambda p: f"wrote {p}",
    "send_email": lambda to: f"emailed {to}",
}
GRANTS = {"researcher": {"read_docs"}, "writer": {"read_docs", "write_file"}}


def call(agent, tool, arg):
    if tool not in GRANTS.get(agent, set()):
        return f"DENIED: {agent} has no {tool}"
    return TOOLS[tool](arg)


if __name__ == "__main__":
    print(call("researcher", "read_docs", "caching"))
    print(call("researcher", "write_file", "a.txt"))
    print(call("writer", "send_email", "x@example.com"))
