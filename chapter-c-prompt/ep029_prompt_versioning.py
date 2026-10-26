"""EP029 · Prompt versioning. Keep versions, score them on fixed cases, roll back if worse."""

VERSIONS = {"v1": "Answer briefly.", "v2": "Answer briefly and cite the source."}
CASES = [("What is 2+2?", "4"), ("Capital of France?", "Paris")]


def score(version):
    # a real eval would call the model; this stub just rewards the 'cite' rule in v2
    return len(CASES) if "cite" in VERSIONS[version] else len(CASES) - 1


if __name__ == "__main__":
    live = "v1"
    for candidate in ("v2",):
        if score(candidate) >= score(live):
            live = candidate
    print("live prompt:", live, "->", VERSIONS[live])
