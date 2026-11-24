"""EP196 · Audit logs: append-only records with a hash chain to spot tampering."""
import hashlib, json

log = []
def record(action):
    prev = log[-1]["hash"] if log else ""
    body = json.dumps({"action": action, "prev": prev}, sort_keys=True)
    log.append({"action": action, "prev": prev, "hash": hashlib.sha256(body.encode()).hexdigest()})

def verify():
    prev = ""
    for r in log:
        body = json.dumps({"action": r["action"], "prev": prev}, sort_keys=True)
        if r["prev"] != prev or r["hash"] != hashlib.sha256(body.encode()).hexdigest():
            return False
        prev = r["hash"]
    return True

record("read file"); record("run tests"); record("edit file")
assert verify()
log[1]["action"] = "rm -rf"
assert not verify()
print("audit logs ok:", len(log), "records")
