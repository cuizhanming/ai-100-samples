"""EP194 · Retries and backoff: exponential delay with a cap and a retry limit."""
def delays(attempts, base=1.0, cap=8.0):
    return [min(cap, base * 2 ** i) for i in range(attempts)]

def call_with_retry(fn, attempts=4):
    for i in range(attempts):
        try:
            return fn(i)
        except TimeoutError:
            if i == attempts - 1:
                raise

flaky = lambda i: "ok" if i >= 2 else (_ for _ in ()).throw(TimeoutError())
assert call_with_retry(flaky) == "ok"
assert delays(5) == [1.0, 2.0, 4.0, 8.0, 8.0]
print("retries and backoff ok:", delays(5))
