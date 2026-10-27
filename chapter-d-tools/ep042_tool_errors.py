"""EP042 · Tool errors and retries. Return errors as results, retry transient faults with a cap."""
import time

calls = {"n": 0}


def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("temporary network error")
    return "ok"


def call_with_retry(fn, attempts=4, base_delay=0.01):
    for i in range(attempts):
        try:
            return {"ok": True, "result": fn(), "attempts": i + 1}
        except ConnectionError as e:
            if i == attempts - 1:
                return {"ok": False, "error": str(e)}
            time.sleep(base_delay * 2 ** i)


if __name__ == "__main__":
    print(call_with_retry(flaky))
