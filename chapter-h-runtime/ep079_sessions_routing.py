"""EP079 · Sessions and routing: one key per conversation keeps histories apart."""


def session_key(channel, chat, is_group):
    return f"{channel}:{'group' if is_group else 'dm'}:{chat}"


store = {}


def handle(channel, chat, is_group, text):
    key = session_key(channel, chat, is_group)
    history = store.setdefault(key, [])
    history.append(text)
    return key, len(history)


if __name__ == "__main__":
    print(handle("discord", "42", False, "my secret plan"))
    print(handle("discord", "42", True, "group hello"))
    print(handle("discord", "42", False, "continue"))
    print(sorted(store))
