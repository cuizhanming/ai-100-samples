"""EP047 · Reflection. Draft, critique against a rule, revise, with a round cap."""


def draft(text, feedback=None):
    return text if feedback is None else text[:50].rstrip() + "..."


def critique(text):
    return None if len(text) <= 50 else "too long: keep it under 50 chars"


def reflect(text, max_rounds=3):
    out, feedback = draft(text), None
    for round_no in range(1, max_rounds + 1):
        feedback = critique(out)
        print(f"round {round_no}: {feedback or 'passes'}")
        if feedback is None:
            break
        out = draft(out, feedback)
    return out


if __name__ == "__main__":
    print(reflect("An agent loop calls a model, runs tools, and repeats until it is done."))
