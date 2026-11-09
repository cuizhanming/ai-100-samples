"""EP125 · Parallel agents and leases: one owner at a time, leases expire."""
import time


class Leases:
    def __init__(self):
        self.held = {}

    def claim(self, resource, owner, ttl, now=None):
        now = time.time() if now is None else now
        cur = self.held.get(resource)
        if cur and cur[1] > now and cur[0] != owner:
            return False
        self.held[resource] = (owner, now + ttl)
        return True

    def release(self, resource, owner):
        if self.held.get(resource, (None,))[0] == owner:
            del self.held[resource]


l = Leases()
assert l.claim("a.py", "agent1", 60, now=0)
assert not l.claim("a.py", "agent2", 60, now=10)
assert l.claim("a.py", "agent2", 60, now=100)  # expired
l.release("a.py", "agent2")
assert "a.py" not in l.held
print("leases ok")
