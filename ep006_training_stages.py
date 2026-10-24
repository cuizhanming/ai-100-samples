"""EP006 · Pretraining vs post-training, as a toy bigram model.
Pretraining: count next-word statistics on broad text. Post-training: reweight toward desired behaviour.
Weights are fixed once training ends; an agent adds knowledge through context instead."""
from collections import Counter, defaultdict

PRETRAIN = "the sky is blue . the sea is deep . the cat is asleep . a question is a request .".split()
POSTTRAIN = "question : what is the sky ? answer : the sky is blue .".split()


def train(model, words, weight=1):
    for a, b in zip(words, words[1:]):
        model[a][b] += weight


def generate(model, start, n=8):
    """Greedy decoding: always take the most likely next word."""
    out = [start]
    for _ in range(n):
        options = model.get(out[-1])
        if not options:
            break
        out.append(options.most_common(1)[0][0])
    return " ".join(out)


if __name__ == "__main__":
    model = defaultdict(Counter)
    train(model, PRETRAIN)
    print("after pretraining :", generate(model, "question"))
    train(model, POSTTRAIN, weight=5)
    print("after post-training:", generate(model, "question"))
