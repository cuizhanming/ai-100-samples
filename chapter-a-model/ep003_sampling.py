"""EP003 · Temperature and sampling. The model scores candidates; temperature reshapes the odds."""
import math
import random


def softmax(logits, temperature=1.0):
    scaled = [x / max(temperature, 1e-6) for x in logits]
    m = max(scaled)
    exps = [math.exp(x - m) for x in scaled]
    total = sum(exps)
    return [e / total for e in exps]


def sample(tokens, logits, temperature=1.0, top_k=None, top_p=None, rng=random):
    probs = softmax(logits, temperature)
    ranked = sorted(zip(tokens, probs), key=lambda t: -t[1])
    if top_k:
        ranked = ranked[:top_k]
    if top_p:
        kept, cum = [], 0.0
        for tok, p in ranked:
            kept.append((tok, p))
            cum += p
            if cum >= top_p:
                break
        ranked = kept
    total = sum(p for _, p in ranked)
    return rng.choices([t for t, _ in ranked], weights=[p / total for _, p in ranked])[0]


if __name__ == "__main__":
    tokens = ["cat", "dog", "fox", "owl"]
    logits = [2.0, 1.2, 0.5, -0.5]
    for t in (0.2, 1.0, 2.0):
        print(f"T={t}:", [f"{tok} {p:.0%}" for tok, p in zip(tokens, softmax(logits, t))])
    rng = random.Random(7)
    print("20 draws at T=1.0:", [sample(tokens, logits, 1.0, rng=rng) for _ in range(20)])
