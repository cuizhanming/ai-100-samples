"""EP156 · Human handoff: pause on risky steps, resume with the human's answer."""
RISKY = {"delete", "deploy", "force-push"}

def run(steps, ask):
    log = []
    for s in steps:
        if s in RISKY and not ask(s):
            log.append(f"stopped at {s}")
            return log
        log.append(f"did {s}")
    return log

assert run(["edit", "test"], ask=lambda s: False) == ["did edit", "did test"]
assert run(["edit", "deploy", "notify"], ask=lambda s: False) == ["did edit", "stopped at deploy"]
assert run(["edit", "deploy"], ask=lambda s: True) == ["did edit", "did deploy"]
print("handoff ok")
