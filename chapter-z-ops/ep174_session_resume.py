"""EP174 · Session resume: save a transcript to disk and reload it."""
import json, os, tempfile

path = os.path.join(tempfile.mkdtemp(), "session.json")
history = [{"role": "user", "text": "add tests"}, {"role": "agent", "text": "done"}]
json.dump(history, open(path, "w"))
assert json.load(open(path)) == history
print("session resume ok")
