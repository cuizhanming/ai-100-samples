"""EP142 · Plugins and extensions: one bundle registers skills, hooks and tools."""
plugin = {
    "name": "team-kit",
    "skills": ["review"],
    "hooks": ["after_edit"],
    "tools": ["lint"],
}
registry = {"skills": [], "hooks": [], "tools": []}


def load(p):
    for kind in registry:
        registry[kind].extend(p.get(kind, []))


load(plugin)
assert registry == {"skills": ["review"], "hooks": ["after_edit"], "tools": ["lint"]}
print(registry)
print("plugin ok")
