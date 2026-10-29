"""EP045 · ReAct. Think, act, observe, repeat with a scripted stand-in for the model."""
TOOLS = {"weather": lambda city: {"Dublin": "11C rain"}.get(city, "unknown")}


def fake_model(history):
    if not any(h[0] == "observe" for h in history):
        return ("act", "weather", "Dublin")
    return ("answer", f"Take a coat: {history[-1][1]}")


def react(question):
    history = [("question", question)]
    while True:
        step = fake_model(history)
        if step[0] == "answer":
            return step[1], history
        _, tool, arg = step
        history += [("act", f"{tool}({arg})"), ("observe", TOOLS[tool](arg))]


if __name__ == "__main__":
    answer, trace = react("Do I need a coat in Dublin?")
    for kind, text in trace:
        print(f"{kind:9}: {text}")
    print("answer   :", answer)
