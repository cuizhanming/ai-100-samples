"""EP132 · Session transcript: append messages to disk, resume in a new run."""
import json, os, tempfile

path = os.path.join(tempfile.mkdtemp(), "session.jsonl")


def append(msg):
    with open(path, "a") as f:
        f.write(json.dumps(msg) + "\n")


def resume():
    with open(path) as f:
        return [json.loads(line) for line in f]


append({"role": "user", "content": "add a test"})
append({"role": "assistant", "content": "done"})
messages = resume()  # a new process would start here
assert len(messages) == 2 and messages[0]["content"] == "add a test"
print("resumed", len(messages), "messages; live processes are not restored")
print("resume ok")
