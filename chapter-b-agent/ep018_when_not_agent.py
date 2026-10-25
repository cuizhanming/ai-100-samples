"""EP018 · When NOT to use an agent. Pick the simplest option that works."""


def choose(steps_known, needs_language, exact_result):
    if steps_known and not needs_language:
        return "plain code"
    if steps_known:
        return "fixed workflow or a single LLM call"
    if exact_result:
        return "plain code or a workflow, with the model only where needed"
    return "agent"


if __name__ == "__main__":
    print(choose(True, False, True))
    print(choose(True, True, False))
    print(choose(False, True, False))
