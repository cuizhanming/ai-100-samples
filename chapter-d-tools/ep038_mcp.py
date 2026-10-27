"""EP038 · MCP. Toy client/server speaking JSON-RPC-style messages (not the real SDK)."""
import json


class ToyServer:
    TOOLS = [{"name": "echo", "description": "Echo text back"}]

    def handle(self, msg):
        m = json.loads(msg)
        if m["method"] == "tools/list":
            return json.dumps({"id": m["id"], "result": self.TOOLS})
        if m["method"] == "tools/call":
            return json.dumps({"id": m["id"], "result": m["params"]["arguments"]["text"]})


if __name__ == "__main__":
    server = ToyServer()
    print(server.handle(json.dumps({"id": 1, "method": "tools/list"})))
    print(server.handle(json.dumps({"id": 2, "method": "tools/call", "params": {"name": "echo", "arguments": {"text": "hi"}}})))
