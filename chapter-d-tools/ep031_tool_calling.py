"""EP031 · Tool calling. The model only requests a call; your code executes it."""
TOOLS = {"add": lambda a, b: a + b}


def fake_model(question):
    # Stand-in for an LLM: emits a structured call instead of running anything.
    return {"tool": "add", "arguments": {"a": 2, "b": 3}}


def run(question):
    call = fake_model(question)
    result = TOOLS[call["tool"]](**call["arguments"])
    return {"call": call, "result": result}


if __name__ == "__main__":
    print(run("what is 2 + 3?"))
