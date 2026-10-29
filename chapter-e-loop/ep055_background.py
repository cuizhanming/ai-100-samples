"""EP055 · Background tasks. Start work, get an id at once, poll for the result."""
import threading
import time
import uuid

TASKS = {}


def start(fn, *args):
    task_id = uuid.uuid4().hex[:8]
    TASKS[task_id] = {"status": "running", "result": None}

    def worker():
        TASKS[task_id]["result"] = fn(*args)
        TASKS[task_id]["status"] = "done"

    threading.Thread(target=worker, daemon=True).start()
    return task_id


def slow_job(n):
    time.sleep(0.2)
    return n * 2


if __name__ == "__main__":
    tid = start(slow_job, 21)
    print("started, status:", TASKS[tid]["status"])
    while TASKS[tid]["status"] != "done":
        time.sleep(0.05)
    print("finished, result:", TASKS[tid]["result"])
