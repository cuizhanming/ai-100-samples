"""EP052 · State machines and graphs. Nodes do work, edges decide what runs next."""


def draft(s):
    s["text"] = "v" + str(s.get("rev", 0) + 1)
    s["rev"] = s.get("rev", 0) + 1


def review(s):
    s["ok"] = s["rev"] >= 2


NODES = {"draft": draft, "review": review}
EDGES = {"draft": lambda s: "review", "review": lambda s: "END" if s["ok"] else "draft"}


def run(state=None, start="draft"):
    state, node, path = state or {}, start, []
    while node != "END":
        NODES[node](state)
        path.append(node)
        node = EDGES[node](state)
    return path, state


if __name__ == "__main__":
    print(run())
