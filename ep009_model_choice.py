"""EP009 · Choosing a model. Pick the cheapest model that passes your eval for the task.
Model names, prices and scores are made up for illustration. Replace them with your own measurements."""

MODELS = [
    {"name": "small", "usd_per_mtok": 0.2, "latency_s": 0.4, "eval": {"classify": 0.95, "plan": 0.55}},
    {"name": "medium", "usd_per_mtok": 2.0, "latency_s": 1.0, "eval": {"classify": 0.97, "plan": 0.80}},
    {"name": "large", "usd_per_mtok": 15.0, "latency_s": 2.5, "eval": {"classify": 0.98, "plan": 0.93}},
]


def choose(task: str, min_score: float):
    passing = [m for m in MODELS if m["eval"][task] >= min_score]
    return min(passing, key=lambda m: m["usd_per_mtok"], default=None)


if __name__ == "__main__":
    for task, bar in (("classify", 0.9), ("plan", 0.9)):
        m = choose(task, bar)
        print(f"{task:9s} needs >= {bar:.0%} -> {m['name'] if m else 'none passes'}")
