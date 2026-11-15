"""EP148 · Retries and errors: retry transient failures with capped backoff."""
class Transient(Exception): pass
class Permanent(Exception): pass

def call_with_retry(fn, max_tries=3, base=0.1, sleep=lambda s: None):
    delays = []
    for attempt in range(max_tries):
        try:
            return fn(attempt), delays
        except Transient:
            if attempt == max_tries - 1:
                raise
            delays.append(base * 2 ** attempt)
            sleep(delays[-1])

flaky = lambda a: "ok" if a == 2 else (_ for _ in ()).throw(Transient())
result, delays = call_with_retry(flaky)
assert result == "ok" and delays == [0.1, 0.2]

def bad(a): raise Permanent("bad request")
try:
    call_with_retry(bad)
except Permanent:
    pass
else:
    raise SystemExit("permanent errors must not be retried")
print("retries ok")
