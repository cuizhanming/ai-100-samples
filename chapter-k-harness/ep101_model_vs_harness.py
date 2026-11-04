"""EP101 · Model vs harness: the model only decides; the harness runs tools and keeps history."""


def toy_model(history):
    """Scripted stand-in for an LLM: asks for one tool, then answers."""
    if not any(m["role"] == "tool" for m in history):
        return {"tool": "add", "args": {"a": 2, "b": 3}}
    return {"text": "The answer is %s." % history[-1]["content"]}


TOOLS = {"add": lambda a, b: a + b}  # the harness owns the tools


def harness(task, max_turns=5):
    history = [{"role": "user", "content": task}]
    for _ in range(max_turns):
        out = toy_model(history)
        if "text" in out:
            return out["text"]
        result = TOOLS[out["tool"]](**out["args"])  # only the harness executes
        history.append({"role": "tool", "content": result})
    return "stopped: turn cap"


if __name__ == "__main__":
    print(harness("What is 2 + 3?"))
