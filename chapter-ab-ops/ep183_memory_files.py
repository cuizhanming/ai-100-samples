"""EP183 · Memory files: project rules are loaded into every new session."""
memory = "Build: make test\nStyle: no trailing spaces"

def start_session(memory_file):
    return [("system", memory_file)] if memory_file else []

assert start_session(memory) == [("system", memory)]
assert start_session("") == []
print("memory files ok: rules persist across sessions")
