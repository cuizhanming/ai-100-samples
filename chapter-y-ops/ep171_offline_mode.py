"""EP171 · Offline mode: a local endpoint with telemetry and web tools off."""
config = {"endpoint": "http://localhost:11434", "telemetry": False, "web_tools": False}

def is_offline(c):
    return c["endpoint"].startswith(("http://localhost", "http://127.0.0.1")) and not c["telemetry"] and not c["web_tools"]

assert is_offline(config)
assert not is_offline({**config, "telemetry": True})
print("offline config ok")
