"""EP198 · Rate-limit awareness: pace calls to stay under a requests-per-window cap."""
def pace(n_calls, limit, window):
    """Return the time each call can start, spacing calls so no window exceeds the limit."""
    gap = window / limit
    return [round(i * gap, 2) for i in range(n_calls)]

starts = pace(6, limit=3, window=6.0)
assert starts == [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
assert all(starts[i + 3] - starts[i] >= 6.0 for i in range(3))
print("rate-limit awareness ok:", starts)
