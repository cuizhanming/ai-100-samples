"""EP118 · MCP Apps: a tool result that points at a UI resource (simplified illustration)."""
tool_meta = {"name": "show_chart", "_meta": {"ui": {"resourceUri": "ui://charts/bar"}}}
resources = {"ui://charts/bar": "<html><body><canvas id=c></canvas></body></html>"}


def host_render(tool):
    uri = tool.get("_meta", {}).get("ui", {}).get("resourceUri")
    return resources[uri] if uri else "(text result only)"


print(host_render(tool_meta))
print(host_render({"name": "plain"}))
assert host_render({"name": "plain"}) == "(text result only)"
