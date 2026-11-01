"""EP078 · Channels: adapters normalize platform events into one message shape."""


def from_discord(raw):
    return {"channel": "discord", "chat": raw["channel_id"], "sender": raw["author"], "text": raw["content"]}


def from_telegram(raw):
    return {"channel": "telegram", "chat": str(raw["chat"]["id"]), "sender": raw["from"]["username"], "text": raw["text"]}


def agent(msg):
    return f"echo from core: {msg['text']}"  # the core never sees platform details


if __name__ == "__main__":
    msgs = [
        from_discord({"channel_id": "42", "author": "ann", "content": "hello"}),
        from_telegram({"chat": {"id": 7}, "from": {"username": "bob"}, "text": "hi"}),
    ]
    for m in msgs:
        print(m["channel"], m["chat"], "->", agent(m))
