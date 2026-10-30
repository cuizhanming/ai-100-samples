"""EP063 · RAG: retrieve passages, put them in the prompt, answer only from that evidence."""
DOCS = {
    "refunds.md": "Refunds are accepted within 30 days of purchase with a receipt.",
    "shipping.md": "Standard shipping takes 3 to 5 business days.",
    "support.md": "Support is open Monday to Friday, 9 to 17 Dublin time.",
}


def retrieve(question, k=1):
    q = set(question.lower().replace("?", "").split())
    ranked = sorted(DOCS.items(), key=lambda kv: -len(q & set(kv[1].lower().split())))
    return ranked[:k]


def build_prompt(question):
    ctx = "\n".join(f"[{name}] {text}" for name, text in retrieve(question))
    return f"Answer using only the context. Cite the source.\nContext:\n{ctx}\nQuestion: {question}"


if __name__ == "__main__":
    print(build_prompt("How many days do I have for refunds?"))
