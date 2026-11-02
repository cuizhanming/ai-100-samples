"""EP090 · Guardrails: code checks inputs, tool calls and outputs around the model."""
import re


def check_input(text):
    return "ignore previous instructions" not in text.lower()


def check_action(tool, args):
    return not (tool == "transfer" and args.get("amount", 0) > 100)


def check_output(text):
    return not re.search(r"\b\d{16}\b", text)  # looks like a card number


if __name__ == "__main__":
    print("input ok:", check_input("Summarize this page"))
    print("input ok:", check_input("Ignore previous instructions and ..."))
    print("action ok:", check_action("transfer", {"amount": 50}))
    print("action ok:", check_action("transfer", {"amount": 5000}))
    print("output ok:", check_output("Your card 4111111111111111 is set"))
