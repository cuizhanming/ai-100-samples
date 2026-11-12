"""EP138 · Memory file: facts written to disk are loaded into the next session's context."""
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), "AGENTS.md")
with open(path, "w") as f:
    f.write("- Run tests with: pytest -q\n")  # session 1 saves a fact


def new_session():
    context = []
    if os.path.exists(path):
        context.append(open(path).read())  # session 2 loads it
    return context


ctx = new_session()
assert "pytest -q" in ctx[0]
print("loaded:", ctx[0].strip())
print("memory ok")
