"""EP113 · Token cost per turn: the context is resent every turn. Prices are illustrative, not real."""
IN, CACHED, OUT = 3.00, 0.30, 15.00  # illustrative $ per million tokens

context, total, total_cached = 2000, 0.0, 0.0
for turn in range(1, 6):
    out = 400
    total += (context * IN + out * OUT) / 1e6
    total_cached += (context * CACHED + out * OUT) / 1e6  # best case: whole prefix cached
    print(f"turn {turn}: context {context} tokens")
    context += out + 800  # answer plus tool output join the history
print(f"no cache: ${total:.4f}  with cache: ${total_cached:.4f}")
