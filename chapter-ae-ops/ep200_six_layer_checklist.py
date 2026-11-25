"""EP200 · The six-layer checklist: score a harness config layer by layer and find the weak one."""
LAYERS = ["model", "loop", "context", "tools", "control", "scale"]
harness = {"model": True, "loop": True, "context": True, "tools": True, "control": False, "scale": True}

weak = [l for l in LAYERS if not harness[l]]
assert weak == ["control"]
print("six-layer checklist ok: weak layers =", weak)
