"""EP149 · Rate limits: honor a retry-after hint and a request budget."""
class Limiter:
    def __init__(self, per_minute):
        self.per_minute, self.used = per_minute, 0

    def request(self):
        if self.used >= self.per_minute:
            return 429, 30  # status, retry-after seconds
        self.used += 1
        return 200, 0

lim = Limiter(per_minute=3)
codes = [lim.request()[0] for _ in range(5)]
assert codes == [200, 200, 200, 429, 429]
assert lim.request() == (429, 30)

# parallel agents share the same budget
shared = Limiter(per_minute=4)
agents = {"a": 0, "b": 0}
for _ in range(3):
    for name in agents:
        if shared.request()[0] == 200:
            agents[name] += 1
assert sum(agents.values()) == 4
print("rate limits ok")
