"""EP175 · MCP server vetting: flag servers that are unpinned or ask for broad scopes."""
servers = [
    {"name": "docs", "version": "1.2.0", "scopes": ["read:docs"]},
    {"name": "shell", "version": "latest", "scopes": ["exec:*"]},
]

def issues(s):
    out = []
    if s["version"] == "latest":
        out.append("unpinned")
    if any(x.endswith("*") for x in s["scopes"]):
        out.append("broad scope")
    return out

assert issues(servers[0]) == [] and issues(servers[1]) == ["unpinned", "broad scope"]
print("vetting ok")
