"""EP016 · Single vs multi-agent. Splitting adds coordination cost; do it only with a reason.
Token numbers are illustrative."""

HANDOFF_OVERHEAD = 300  # tokens spent briefing each extra agent


def cost(tasks, tokens_per_task=1000, agents=1):
    return tasks * tokens_per_task + (agents - 1) * HANDOFF_OVERHEAD


if __name__ == "__main__":
    print("single :", cost(4, agents=1), "tokens, sequential")
    print("multi  :", cost(4, agents=4), "tokens, but the 4 tasks can run in parallel")
    print("Multi-agent costs more tokens; it buys parallelism or cleaner context.")
