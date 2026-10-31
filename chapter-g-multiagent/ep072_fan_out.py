"""EP072 · Parallel fan-out and collect with a thread pool."""
import time
from concurrent.futures import ThreadPoolExecutor


def worker(topic):
    time.sleep(0.2)  # stands in for a model call
    return f"notes on {topic}"


if __name__ == "__main__":
    topics = ["a", "b", "c", "d"]
    t0 = time.time()
    with ThreadPoolExecutor() as pool:
        results = list(pool.map(worker, topics))
    print(results)
    print(f"parallel {time.time() - t0:.1f}s vs sequential ~{0.2 * len(topics):.1f}s")
