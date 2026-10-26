"""EP030 · Context rot. Noise piles up; trimming keeps the key facts findable. Numbers are illustrative."""


def signal_ratio(messages):
    return round(sum(m["useful"] for m in messages) / len(messages), 2)


def trim(messages, keep=3):
    useful = [m for m in messages if m["useful"]]
    return useful[-keep:]


if __name__ == "__main__":
    history = [{"text": f"turn {i}", "useful": i % 5 == 0} for i in range(1, 31)]
    print("before:", len(history), "messages, signal", signal_ratio(history))
    kept = trim(history)
    print("after :", len(kept), "messages, signal", signal_ratio(kept))
