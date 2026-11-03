"""EP095 · Build your first agent: a minimal ask / act / repeat loop with a turn cap and a scripted toy model."""

TOOLS = {"add": lambda a, b: a + b}


def toy_model(messages):
    # Scripted stand-in for an LLM: request one tool call, then answer from its result.
    last = messages[-1]
    if last["role"] == "user":
        return {"tool": "add", "args": {"a": 2, "b": 3}}
    return {"answer": f"The sum is {last['content']}"}


def run(task, max_turns=5):
    messages = [{"role": "user", "content": task}]
    for turn in range(1, max_turns + 1):
        reply = toy_model(messages)
        if "answer" in reply:
            return reply["answer"], turn
        result = TOOLS[reply["tool"]](**reply["args"])
        messages.append({"role": "tool", "content": result})
    return "stopped: turn cap reached", max_turns


if __name__ == "__main__":
    print(run("What is 2 + 3?"))
