"""EP020 · Persona and soul files. Identity is loaded from a file at start-up."""
import os
import tempfile


def load_persona(path):
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "SOUL.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Soul\nName: Hawk\nTone: calm, precise\nBoundary: ask before anything public\n")
        for session in (1, 2):  # a new session has no memory, the file restores the same identity
            print("session", session, "->", load_persona(path).splitlines()[1])
