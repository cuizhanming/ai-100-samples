"""EP094 · Failure postmortems: find the first wrong step in a trace and turn it into a regression test."""

TRACE = [
    {"step": 1, "tool": "search", "ok": True},
    {"step": 2, "tool": "parse", "ok": False, "error": "empty result"},
    {"step": 3, "tool": "summarize", "ok": False, "error": "no input"},
]


def first_failure(trace):
    return next((s for s in trace if not s["ok"]), None)


def regression_test(step):
    return f"assert tool {step['tool']!r} handles error {step['error']!r}"


if __name__ == "__main__":
    bad = first_failure(TRACE)
    print("root cause at step", bad["step"], "->", bad["tool"])  # later failures are side effects
    print("new test:", regression_test(bad))
