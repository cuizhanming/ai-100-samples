"""EP108 · Instruction files: walk from the repo root to the working folder and join the rules found."""
import os, tempfile

root = tempfile.mkdtemp()
os.makedirs(os.path.join(root, "svc", "api"))
for rel, text in {"AGENTS.md": "Use type hints.", "svc/AGENTS.md": "Run `make test`.", "svc/api/AGENTS.md": "Never edit generated/."}.items():
    open(os.path.join(root, rel), "w").write(text)


def load_rules(root, cwd, name="AGENTS.md"):
    rules, parts = [], os.path.relpath(cwd, root).split(os.sep)
    for i in range(len(parts) + 1):
        path = os.path.join(root, *parts[:i], name)
        if os.path.exists(path):
            rules.append(open(path).read())
    return rules


for r in load_rules(root, os.path.join(root, "svc", "api")):
    print("-", r)
