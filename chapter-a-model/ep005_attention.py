"""EP005 · Attention. Each token scores every other token, then mixes their values by those weights.
Vectors are hand-made toys; real models learn them during training."""
import math


def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    s = sum(e)
    return [v / s for v in e]


def attention(query, keys, values):
    d = len(query)
    scores = [sum(q * k for q, k in zip(query, key)) / math.sqrt(d) for key in keys]
    weights = softmax(scores)
    mixed = [sum(w * v[i] for w, v in zip(weights, values)) for i in range(len(values[0]))]
    return weights, mixed


if __name__ == "__main__":
    words = ["trophy", "bag", "big"]
    keys = [[1.0, 0.0], [0.0, 1.0], [0.6, 0.2]]
    values = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    query_it = [1.0, 0.1]  # the token "it" asks: which noun is big?
    weights, mixed = attention(query_it, keys, values)
    for w, p in zip(words, weights):
        print(f"{w:7s} {p:.2f}")
    print("mixed value for 'it':", [round(x, 2) for x in mixed])
