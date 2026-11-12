"""EP137 · Verification loop: edit, run the check, feed failures back, cap the retries."""


def check(code):
    return [] if code["add"](2, 3) == 5 else ["add(2,3) != 5"]


attempts = [{"add": lambda a, b: a - b}, {"add": lambda a, b: a + b}]  # model's tries
MAX_RETRIES = 3
for i, code in enumerate(attempts[:MAX_RETRIES], 1):
    errors = check(code)
    print(f"attempt {i}:", errors or "pass")
    if not errors:
        break
assert not errors and i == 2
print("verify ok")
