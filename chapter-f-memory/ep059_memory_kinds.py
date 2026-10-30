"""EP059 · Episodic, semantic, procedural memory kept in separate buckets."""
memory = {"episodic": [], "semantic": {}, "procedural": []}


def remember(kind, item):
    if kind == "semantic":
        memory[kind][item[0]] = item[1]
    else:
        memory[kind].append(item)


def build_prompt(task):
    rules = "\n".join(f"- {r}" for r in memory["procedural"])
    facts = "; ".join(f"{k}={v}" for k, v in memory["semantic"].items())
    past = memory["episodic"][-1] if memory["episodic"] else "none"
    return f"Task: {task}\nRules:\n{rules}\nFacts: {facts}\nLast similar run: {past}"


if __name__ == "__main__":
    remember("episodic", "2026-10-28: summary was too long, user asked to shorten")
    remember("semantic", ("language", "English"))
    remember("procedural", "Keep summaries under 5 bullets")
    print(build_prompt("summarise the report"))
