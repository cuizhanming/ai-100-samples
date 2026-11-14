"""EP146 · Managed settings: higher layers override lower ones."""
LAYERS = [  # lowest to highest priority
    {"web": "allow", "shell": "ask"},          # user
    {"shell": "ask"},                          # project
    {"web": "deny"},                           # managed
]


def resolve(layers):
    out = {}
    for layer in layers:
        out.update(layer)
    return out


cfg = resolve(LAYERS)
assert cfg == {"web": "deny", "shell": "ask"}
print("managed ok", cfg)
