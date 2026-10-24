"""EP008 · Hallucination. Ground answers in sources and refuse when nothing supports the claim."""
import re

SOURCES = {
    "doc1": "The context window is the token budget for one model call.",
    "doc2": "Temperature changes randomness in sampling, not correctness.",
}


def words(text):
    return set(re.findall(r"[a-z]+", text.lower()))


def supported_by(claim: str, sources=SOURCES, threshold=0.6):
    claim_words = words(claim)
    best_id, best = None, 0.0
    for sid, text in sources.items():
        overlap = len(claim_words & words(text)) / max(len(claim_words), 1)
        if overlap > best:
            best_id, best = sid, overlap
    return (best_id, best) if best >= threshold else (None, best)


def answer(claim: str):
    sid, score = supported_by(claim)
    return f"{claim} [source: {sid}]" if sid else "I don't know: no source supports that."


if __name__ == "__main__":
    print(answer("Temperature changes randomness in sampling"))
    print(answer("The 2019 study by Smith proved X"))
