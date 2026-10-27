"""EP044 · Tool search. Load only matching tool definitions instead of the whole catalog."""
CATALOG = {f"tool_{i}": f"description for helper {i}" for i in range(100)}
CATALOG["send_email"] = "send an email message to a person"
CATALOG["create_invoice"] = "create an invoice for a customer"


def search(query, limit=2):
    words = set(query.lower().split())
    scored = sorted(CATALOG, key=lambda n: -len(words & set(CATALOG[n].split())))
    return scored[:limit]


if __name__ == "__main__":
    print("catalog size :", len(CATALOG))
    print("loaded       :", search("send an email"))
