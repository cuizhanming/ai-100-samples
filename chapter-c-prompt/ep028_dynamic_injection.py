"""EP028 · Dynamic context injection. Add only the relevant facts, with their source, per request."""

FACTS = {"billing": ["Plan: Pro", "Renews on the 1st"], "shipping": ["Order 42 left the depot"]}


def inject(request):
    topic = "billing" if "invoice" in request or "plan" in request else "shipping"
    ctx = "\n".join(f"[source: crm/{topic}] {f}" for f in FACTS[topic])
    return f"Context:\n{ctx}\n\nUser: {request}"


if __name__ == "__main__":
    print(inject("Why is my invoice higher?"))
    print()
    print(inject("Where is my parcel?"))
