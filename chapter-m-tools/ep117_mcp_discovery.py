"""EP117 · MCP servers: tools/list discovery then tools/call (simplified, in-process)."""
import json

TOOLS = {"add": {"description": "Add two numbers",
                 "inputSchema": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}}}}}


def handle(req):
    if req["method"] == "tools/list":
        return {"tools": [{"name": k, **v} for k, v in TOOLS.items()]}
    if req["method"] == "tools/call":
        a = req["params"]["arguments"]
        return {"content": [{"type": "text", "text": str(a["a"] + a["b"])}]}


listed = handle({"method": "tools/list"})
print(json.dumps(listed))
res = handle({"method": "tools/call", "params": {"name": "add", "arguments": {"a": 2, "b": 3}}})
assert res["content"][0]["text"] == "5"
print(res)
