"""EP025 · Context compaction. Summarise old turns, keep recent ones and pinned facts."""


def compact(messages, keep_recent=2, pinned=()):
    if len(messages) <= keep_recent:
        return messages
    old, recent = messages[:-keep_recent], messages[-keep_recent:]
    summary = f"Summary of {len(old)} earlier messages. Pinned: " + "; ".join(pinned)  # a real agent asks the model here
    return [summary] + recent


if __name__ == "__main__":
    msgs = [f"msg {i}" for i in range(1, 9)]
    print(compact(msgs, keep_recent=2, pinned=("deadline is Friday",)))
