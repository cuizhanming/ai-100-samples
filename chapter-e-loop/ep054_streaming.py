"""EP054 · Streaming. Yield events as they happen instead of one final reply."""


def agent(question):
    yield ("step", "calling search tool")
    yield ("step", "reading 3 results")
    for word in "Streaming shows progress early.".split():
        yield ("token", word)
    yield ("end", "")


if __name__ == "__main__":
    text = []
    for kind, data in agent("why stream?"):
        if kind == "step":
            print("[step]", data)
        elif kind == "token":
            text.append(data)
    print(" ".join(text))
