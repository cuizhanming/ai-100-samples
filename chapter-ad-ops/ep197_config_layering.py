"""EP197 · Config layering: defaults < user < project < command line; later layers win."""
def merge(*layers):
    out = {}
    for layer in layers:
        out.update(layer)
    return out

defaults = {"model": "base", "approval": "ask", "theme": "dark"}
user = {"theme": "light"}
project = {"approval": "allowlist"}
cli = {"model": "fast"}
cfg = merge(defaults, user, project, cli)
assert cfg == {"model": "fast", "approval": "allowlist", "theme": "light"}
print("config layering ok:", cfg)
