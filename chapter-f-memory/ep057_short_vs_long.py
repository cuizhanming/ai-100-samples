"""EP057 · Short vs long-term memory. The window forgets between sessions; a store persists."""
import json
import os
import tempfile

WINDOW = 3  # keep only the last N messages (illustrative)


def new_session(store_path):
    long_term = json.load(open(store_path)) if os.path.exists(store_path) else {}
    return {"window": [], "long_term": long_term, "path": store_path}


def say(s, text):
    s["window"] = (s["window"] + [text])[-WINDOW:]
    if text.startswith("remember "):
        key, _, val = text[9:].partition("=")
        s["long_term"][key.strip()] = val.strip()
        json.dump(s["long_term"], open(s["path"], "w"))


if __name__ == "__main__":
    path = os.path.join(tempfile.mkdtemp(), "memory.json")
    s1 = new_session(path)
    for m in ["hi", "remember name=Zhan", "ok", "weather?", "thanks"]:
        say(s1, m)
    print("session 1 window:", s1["window"])
    s2 = new_session(path)
    print("session 2 window:", s2["window"], "| long-term:", s2["long_term"])
