"""EP086 · Secrets and credentials: tools read keys from the environment; prompts and logs never see them."""
import os
import re

os.environ.setdefault("DEMO_API_KEY", "sk-demo-1234567890")  # stand-in; real keys come from a vault or env


def tool_call_api():
    key = os.environ["DEMO_API_KEY"]  # read at call time, inside the tool
    return f"called API with a key of length {len(key)}"


def redact(text):
    return re.sub(r"sk-[A-Za-z0-9-]+", "sk-***", text)


if __name__ == "__main__":
    print(tool_call_api())
    print(redact("log line leaked sk-demo-1234567890 by mistake"))
