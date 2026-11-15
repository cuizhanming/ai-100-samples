"""EP150 · Embedding with an SDK: drive an agent loop from code and stream events."""
def fake_agent(prompt):
    yield {"type": "text", "text": f"plan for: {prompt}"}
    yield {"type": "tool", "name": "read"}
    yield {"type": "done"}

events = []
for ev in fake_agent("fix the test"):
    events.append(ev["type"])
    if ev["type"] == "tool":
        assert ev["name"] in {"read", "edit"}  # your code owns the limits

assert events == ["text", "tool", "done"]
print("sdk ok")
