"""EP067 · Knowledge graph: triples plus a multi-hop traversal."""
TRIPLES = [
    ("Ada", "works_at", "Acme"),
    ("Acme", "located_in", "Dublin"),
    ("Bob", "works_at", "Acme"),
    ("Dublin", "capital_of", "Ireland"),
]


def neighbours(node, rel):
    return [o for s, r, o in TRIPLES if s == node and r == rel]


def where_does_work(person):
    """Two hops: person -> company -> city."""
    return [city for co in neighbours(person, "works_at") for city in neighbours(co, "located_in")]


if __name__ == "__main__":
    print("Ada works in:", where_does_work("Ada"))
    print("Colleagues of Ada:", [s for s, r, o in TRIPLES if r == "works_at" and o == "Acme" and s != "Ada"])
