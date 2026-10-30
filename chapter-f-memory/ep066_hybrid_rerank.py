"""EP066 · Hybrid search: merge keyword and vector rankings with reciprocal rank fusion, then rerank."""
DOCS = {"a": "error E1042 in payment service", "b": "payments fail with timeouts", "c": "how to bake bread"}

KEYWORD = ["a", "b", "c"]  # pretend BM25 ranking for "E1042 payment"
VECTOR = ["b", "a", "c"]  # pretend embedding ranking


def rrf(*rankings, k=60):
    scores = {}
    for r in rankings:
        for pos, doc in enumerate(r):
            scores[doc] = scores.get(doc, 0) + 1 / (k + pos + 1)
    return sorted(scores, key=scores.get, reverse=True)


def rerank(query, ids):
    """Stand-in for a cross-encoder: reward exact term matches."""
    terms = query.lower().split()
    return sorted(ids, key=lambda i: -sum(t in DOCS[i].lower() for t in terms))


if __name__ == "__main__":
    fused = rrf(KEYWORD, VECTOR)
    print("fused:", fused)
    print("reranked:", rerank("E1042 payment", fused[:2]))
