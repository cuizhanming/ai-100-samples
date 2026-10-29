"""EP051 · Interrupts and steering. Check a message queue between steps, keep progress."""
from collections import deque


def run(task_steps, inbox):
    done = []
    steps = deque(task_steps)
    while steps:
        if inbox:
            note = inbox.popleft()
            steps.appendleft(f"adjust: {note}")
        done.append(steps.popleft())
    return done


if __name__ == "__main__":
    print(run(["search", "summarize", "send"], deque(["only use 2026 sources"])))
