"""EP026 · Prompt caching. Only an unchanged prefix can be reused. Prices are illustrative."""

PRICE, READ, WRITE = 1.0, 0.1, 1.25  # relative cost per token: plain input, cache read, cache write


def cost(prompt_tokens, cached_prefix, hit):
    if hit:
        return cached_prefix * READ + (prompt_tokens - cached_prefix) * PRICE
    return cached_prefix * WRITE + (prompt_tokens - cached_prefix) * PRICE


def prefix_matches(a, b):
    return a == b


if __name__ == "__main__":
    stable = "system+tools"
    print("first call :", cost(5000, 4000, hit=False))
    print("second call:", cost(5000, 4000, hit=prefix_matches(stable, "system+tools")))
    print("prefix edited:", cost(5000, 4000, hit=prefix_matches(stable, "NEW system+tools")))
