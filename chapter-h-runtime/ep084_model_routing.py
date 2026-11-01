"""EP084 · Model routing and fallbacks: pick a model by difficulty, fall back on error."""
MODELS = {"small": 0.1, "large": 1.0}  # illustrative relative cost


def route(task):
    return "large" if len(task.split()) > 8 or "prove" in task else "small"


def call(model, task, down=()):
    if model in down:
        raise RuntimeError(f"{model} unavailable")
    return f"{model} answered: {task[:20]}"


def run(task, down=()):
    order = [route(task)] + [m for m in MODELS if m != route(task)]
    for m in order:
        try:
            return call(m, task, down)
        except RuntimeError as e:
            print("fallback:", e)
    raise SystemExit("all models failed")


if __name__ == "__main__":
    print(run("summarize this"))
    print(run("prove that this long and complicated claim about routing holds in general", down=("large",)))
