"""EP015 · Framework landscape. Compare by control model, language and shape, not by logo.
The entries are a rough teaching summary. Check each project's docs for current facts."""

FRAMEWORKS = [
    {"name": "Microsoft Agent Framework", "shape": "library", "control": "agents + workflows", "languages": ["Python", ".NET"]},
    {"name": "Claude Agent SDK", "shape": "SDK", "control": "agent loop", "languages": ["Python", "TypeScript"]},
    {"name": "LangGraph", "shape": "library", "control": "graph", "languages": ["Python", "JavaScript"]},
    {"name": "OpenClaw", "shape": "service", "control": "gateway runtime", "languages": []},
]


def pick(language=None, shape=None):
    return [f["name"] for f in FRAMEWORKS
            if (language is None or language in f["languages"]) and (shape is None or f["shape"] == shape)]


if __name__ == "__main__":
    print("Python:", pick(language="Python"))
    print("services:", pick(shape="service"))
