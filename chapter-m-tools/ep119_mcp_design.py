"""EP119 · Designing a good MCP: 1:1 endpoint proxy vs one task-level tool (illustrative sizes)."""
import json

endpoints = [f"get_order_{i}" for i in range(50)]
proxy = [{"name": n, "description": "GET /orders"} for n in endpoints]
task = [{"name": "track_order", "description": "Find an order by id and return its status and ETA"}]
print(f"1:1 proxy tools: {len(proxy)} ({len(json.dumps(proxy))} chars) | task-level: {len(task)} ({len(json.dumps(task))} chars)")
assert len(json.dumps(task)) < len(json.dumps(proxy))
