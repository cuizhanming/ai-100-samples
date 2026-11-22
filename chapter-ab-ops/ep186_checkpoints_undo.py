"""EP186 · Checkpoints and undo: snapshot before edits, rewind restores the snapshot."""
import copy

files = {"a.py": "v1"}
checkpoints = [copy.deepcopy(files)]
files["a.py"] = "broken"
files = copy.deepcopy(checkpoints[-1])

assert files["a.py"] == "v1"
print("checkpoint ok: rewound to v1")
