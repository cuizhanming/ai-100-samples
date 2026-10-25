"""EP014 · Anatomy of a framework. The ten layers, and what a toy framework covers."""

LAYERS = ["Model", "Prompt & Context", "Tools", "Loop & Planning", "Memory", "Knowledge / RAG",
          "Multi-agent", "Runtime & Gateway", "Safety / Evals / Observability", "Ship & Operate"]


def coverage(provided):
    return {layer: layer in provided for layer in LAYERS}


if __name__ == "__main__":
    toy = {"Model", "Prompt & Context", "Tools", "Loop & Planning"}
    for layer, covered in coverage(toy).items():
        print(("[x] " if covered else "[ ] ") + layer)
    print("The unchecked layers are still your design work.")
