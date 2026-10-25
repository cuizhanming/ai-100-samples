"""EP011 · What is an agent. Model + tools + loop, with a scripted fake model so it runs offline."""

TOOLS = {"add": lambda a, b: a + b}


def fake_model(history):
    """Stands in for an LLM: asks for a tool first, then answers from the tool result."""
    if not any(m["role"] == "tool" for m in history):
        return {"tool": "add", "args": {"a": 2, "b": 3}}
    return {"answer": f"The sum is {history[-1]['content']}."}


def agent(goal, max_steps=5):
    history = [{"role": "user", "content": goal}]
    for _ in range(max_steps):
        step = fake_model(history)
        if "answer" in step:
            return step["answer"]
        result = TOOLS[step["tool"]](**step["args"])
        history.append({"role": "tool", "content": result})
    return "stopped: max steps"


if __name__ == "__main__":
    print(agent("What is 2 + 3?"))
