"""EP195 · Task queues: run queued tasks one at a time, in priority then arrival order."""
import heapq

q, seq = [], 0
def add(priority, name):
    global seq
    heapq.heappush(q, (priority, seq, name))
    seq += 1

add(2, "lint"); add(1, "fix bug"); add(2, "docs"); add(1, "test")
order = [heapq.heappop(q)[2] for _ in range(len(q))]
assert order == ["fix bug", "test", "lint", "docs"]
print("task queues ok:", order)
