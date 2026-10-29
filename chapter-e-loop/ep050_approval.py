"""EP050 · Human-in-the-loop approval. Reads run freely, risky actions wait for a decision."""
RISKY = {"delete_file", "send_payment"}


def call(tool, arg, approve):
    if tool in RISKY and not approve(tool, arg):
        return f"{tool}({arg}): rejected by human"
    return f"{tool}({arg}): executed"


if __name__ == "__main__":
    deny_all = lambda tool, arg: False
    allow_small = lambda tool, arg: arg < 100
    print(call("read_file", "notes.txt", deny_all))
    print(call("send_payment", 5000, allow_small))
    print(call("send_payment", 20, allow_small))
