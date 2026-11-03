"""EP098 · Self-improving agents: lessons become notes only after a test passes (a review gate)."""

NOTES = []


def propose(lesson, regression_test):
    if regression_test(lesson):
        NOTES.append(lesson)  # in practice: a versioned file, reviewed by a human
        return "accepted"
    return "rejected"


if __name__ == "__main__":
    print(propose("Retry search once on empty result", lambda l: "retry" in l.lower()))
    print(propose("Delete the logs to save space", lambda l: "delete" not in l.lower()))
    print("notes:", NOTES)
