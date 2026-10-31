"""EP069 · Orchestrator-worker: the lead splits a task, workers run, the lead merges."""


def worker(name, piece):
    return f"{name}: summarized '{piece}'"


def orchestrate(task):
    pieces = [p.strip() for p in task.split(",")]
    results = [worker(f"worker-{i + 1}", p) for i, p in enumerate(pieces)]
    return {"plan": pieces, "results": results, "answer": " | ".join(results)}


if __name__ == "__main__":
    print(orchestrate("pricing, competitors, risks"))
