"""EP104 · What the harness sends each turn: the full request is rebuilt, so it grows with the history."""
import json

SYSTEM = "You are a coding agent. Follow AGENTS.md."
INSTRUCTIONS = "Use tabs. Run tests before finishing."
TOOLS = [{"name": "read_file", "description": "Read a file"}, {"name": "run", "description": "Run a shell command"}]


def build_request(history):
    return {"system": SYSTEM + "\n" + INSTRUCTIONS, "tools": TOOLS, "messages": history}


if __name__ == "__main__":
    history = []
    for turn in range(1, 5):
        history.append({"role": "user" if turn == 1 else "tool", "content": "x" * 200 * turn})  # illustrative sizes
        size = len(json.dumps(build_request(history)))
        print(f"turn {turn}: {len(history)} messages, request {size} bytes")
