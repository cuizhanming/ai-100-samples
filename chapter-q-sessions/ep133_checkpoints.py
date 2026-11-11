"""EP133 · Checkpoints: snapshot files before an edit, rewind restores them."""
import copy

files = {"app.py": "print('v1')"}
checkpoints = []


def checkpoint():
    checkpoints.append(copy.deepcopy(files))


def rewind():
    files.clear()
    files.update(checkpoints.pop())


checkpoint()
files["app.py"] = "print('broken')"
rewind()
assert files["app.py"] == "print('v1')"
print("rewound file:", files["app.py"], "(shell side effects would not be undone)")
print("checkpoints ok")
