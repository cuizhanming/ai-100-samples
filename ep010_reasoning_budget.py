"""EP010 · Reasoning models. Thinking tokens cost output tokens and latency.
Numbers are illustrative. Check your provider for real pricing and thinking-budget settings."""

PRICE_OUT_PER_MTOK = 10.0
TOKENS_PER_SECOND = 80


def run_cost(answer_tokens: int, thinking_tokens: int = 0):
    out = answer_tokens + thinking_tokens  # thinking is usually billed as output
    return {
        "output_tokens": out,
        "usd": out / 1_000_000 * PRICE_OUT_PER_MTOK,
        "seconds": out / TOKENS_PER_SECOND,
    }


if __name__ == "__main__":
    standard = run_cost(answer_tokens=150)
    reasoning = run_cost(answer_tokens=150, thinking_tokens=4000)
    print("standard :", standard)
    print("reasoning:", reasoning)
    print(f"reasoning costs {reasoning['usd'] / standard['usd']:.0f}x and takes {reasoning['seconds'] / standard['seconds']:.0f}x longer here")
