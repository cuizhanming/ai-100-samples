"""EP102 · Why harnesses replaced frameworks: a hand-wired pipeline vs a loop that lets the model pick steps."""

TOOLS = {"search": lambda q: f"results for {q}", "calc": lambda q: str(eval(q, {"__builtins__": {}}))}


def pipeline(task):
    """Hand-wired: always search, then answer. A math task is handled badly."""
    return TOOLS["search"](task)


def toy_model(task, seen):
    """Scripted model: picks the tool that matches the task."""
    if seen:
        return {"text": seen[-1]}
    return {"tool": "calc", "arg": task} if task[0].isdigit() else {"tool": "search", "arg": task}


def loop(task, max_turns=4):
    seen = []
    for _ in range(max_turns):
        out = toy_model(task, seen)
        if "text" in out:
            return out["text"]
        seen.append(TOOLS[out["tool"]](out["arg"]))
    return "stopped"


if __name__ == "__main__":
    for t in ("harness news", "6*7"):
        print(f"{t!r:15} pipeline={pipeline(t)!r:28} loop={loop(t)!r}")
