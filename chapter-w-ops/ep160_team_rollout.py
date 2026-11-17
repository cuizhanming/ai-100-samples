"""EP160 · Team rollouts: ship a config to a growing share of users, stop on errors."""
import hashlib

def in_rollout(user, percent):
    bucket = int(hashlib.sha256(user.encode()).hexdigest(), 16) % 100
    return bucket < percent

users = [f"user{i}" for i in range(200)]
stages = [5, 25, 100]
prev = set()
for pct in stages:
    cur = {u for u in users if in_rollout(u, pct)}
    assert prev <= cur  # a wider stage keeps earlier users
    prev = cur
assert len(prev) == 200
assert 0 < sum(in_rollout(u, 25) for u in users) < 200
print("team rollout ok")
