"""EP100 · The full map: the ten layers of an agent and where a symptom points."""

LAYERS = ["Model", "Prompt & Context", "Tools", "Loop & Planning", "Memory",
          "Knowledge / RAG", "Multi-agent", "Runtime & Gateway", "Safety / Evals / Observability", "Ship & Operate"]

SYMPTOMS = {
    "makes up facts": 1,
    "wrong tool arguments": 3,
    "loops forever": 4,
    "forgets yesterday": 5,
    "obeys a web page": 9,
    "bill is too high": 9,
}

if __name__ == "__main__":
    for symptom, idx in SYMPTOMS.items():
        print(f"{symptom:<22} -> layer {idx}: {LAYERS[idx - 1]}")
