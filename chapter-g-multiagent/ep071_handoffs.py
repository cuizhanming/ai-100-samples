"""EP071 · Handoffs: control moves to another agent, which answers the user."""
AGENTS = {
    "triage": lambda q: ("billing", q) if "invoice" in q else ("triage", "How can I help?"),
    "billing": lambda q: ("billing", f"Billing agent: checking '{q}'"),
}


def run(question):
    current = "triage"
    nxt, out = AGENTS[current](question)
    if nxt != current:  # handoff: ownership transfers, no return to triage
        current = nxt
        _, out = AGENTS[current](question)
    return current, out


if __name__ == "__main__":
    print(run("where is my invoice?"))
