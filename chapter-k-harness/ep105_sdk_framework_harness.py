"""EP105 · Harness vs framework vs SDK: count who owns the control flow in each style."""


def model(prompt):
    """Stand-in model call. Returns a tool request while no result is present."""
    return {"tool": "now"} if "RESULT" not in prompt else {"text": "done"}


def sdk(prompt):
    """SDK: you get exactly one model call; everything else is yours."""
    return model(prompt)


def framework(prompt):
    """Framework: you wire the steps (a fixed two-node graph)."""
    first = model(prompt)
    return model(prompt + " RESULT=" + first["tool"])


def harness(prompt, max_turns=5):
    """Harness: a ready loop decides when to stop."""
    for turns in range(1, max_turns + 1):
        out = model(prompt)
        if "text" in out:
            return out, turns
        prompt += " RESULT=" + out["tool"]
    return None, max_turns


if __name__ == "__main__":
    print("sdk      :", sdk("what time"))
    print("framework:", framework("what time"))
    print("harness  :", harness("what time"))
