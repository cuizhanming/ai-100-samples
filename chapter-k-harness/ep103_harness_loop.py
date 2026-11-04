"""EP103 · The harness loop: call the model, run requested tools, append results, repeat until no tool is requested."""

SCRIPT = [
    {"tool": "read_file", "args": {"path": "notes.txt"}},
    {"tool": "word_count", "args": {"text": "agents are loops"}},
    {"text": "notes.txt has 3 words."},
]
TOOLS = {"read_file": lambda path: "agents are loops", "word_count": lambda text: len(text.split())}


def run(max_turns=6):
    history = []
    for turn, out in enumerate(SCRIPT[:max_turns], 1):  # the scripted model replies in order
        if "text" in out:
            print(f"turn {turn}: final answer -> {out['text']}")
            return history
        result = TOOLS[out["tool"]](**out["args"])
        history.append((out["tool"], result))
        print(f"turn {turn}: model asked {out['tool']} -> harness ran it -> {result!r}")
    print("stopped: turn cap")
    return history


if __name__ == "__main__":
    run()
