"""EP114 · Built-in tools: a tiny registry with read, edit, shell and search."""
import pathlib
import subprocess
import tempfile

root = pathlib.Path(tempfile.mkdtemp())
(root / "a.txt").write_text("hello world\n")

TOOLS = {
    "read": lambda path: (root / path).read_text(),
    "edit": lambda path, old, new: (root / path).write_text((root / path).read_text().replace(old, new, 1)),
    "shell": lambda cmd: subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True).stdout,
    "search": lambda text: [p.name for p in root.glob("*") if text in p.read_text()],
}

TOOLS["edit"]("a.txt", "world", "harness")
print(TOOLS["read"]("a.txt").strip())
print(TOOLS["search"]("harness"), TOOLS["shell"]("ls").split())
