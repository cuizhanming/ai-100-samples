"""EP033 · Tool descriptions. A naive keyword matcher picks tools from descriptions only."""
TOOLS = {
    "search_docs": "Search internal documentation for how-to answers. Use for product questions.",
    "query_sales": "Run a read-only sales query. Use for revenue and order numbers.",
    "tool2": "Does stuff.",
}


def pick(task):
    words = set(task.lower().split())
    score = {n: len(words & set(d.lower().replace(".", "").split())) for n, d in TOOLS.items()}
    return max(score, key=score.get), score


if __name__ == "__main__":
    print(pick("show revenue and order numbers"))
