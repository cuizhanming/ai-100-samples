"""EP097 · Ship checklist: a release gate that blocks launch until every item is checked."""

CHECKLIST = {
    "evals pass on a fixed task set": True,
    "permissions and allow-list set": True,
    "turn cap and token budget set": True,
    "secrets kept out of prompts": True,
    "tracing and alerts on": True,
    "rollback plan written": False,
}


def gate(items):
    missing = [name for name, ok in items.items() if not ok]
    return (not missing), missing


if __name__ == "__main__":
    ok, missing = gate(CHECKLIST)
    print("SHIP" if ok else "HOLD", missing)
