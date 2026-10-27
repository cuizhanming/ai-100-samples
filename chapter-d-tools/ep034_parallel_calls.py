"""EP034 · Parallel tool calls. Independent calls run together; total time is the slowest one."""
import time
from concurrent.futures import ThreadPoolExecutor


def slow_tool(name, seconds=0.3):
    time.sleep(seconds)
    return name


if __name__ == "__main__":
    calls = ["weather", "news", "stocks"]
    t = time.time()
    [slow_tool(c) for c in calls]
    print("sequential:", round(time.time() - t, 1), "s")
    t = time.time()
    with ThreadPoolExecutor() as pool:
        list(pool.map(slow_tool, calls))
    print("parallel  :", round(time.time() - t, 1), "s")
