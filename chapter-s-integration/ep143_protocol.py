"""EP143 · Agent protocols: any client works with any agent that speaks the same messages."""
import json


class Agent:
    def __init__(self, name):
        self.name = name

    def handle(self, msg):
        req = json.loads(msg)
        return json.dumps({"id": req["id"], "result": f"{self.name} ran {req['method']}"})


def client(agent):
    reply = json.loads(agent.handle(json.dumps({"id": 1, "method": "prompt"})))
    return reply["result"]


for a in (Agent("agent-a"), Agent("agent-b")):
    assert client(a).endswith("ran prompt")
print("protocol ok")
