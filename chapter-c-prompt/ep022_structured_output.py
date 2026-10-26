"""EP022 · Structured output. A schema fixes the shape; you still validate the values."""
import json

SCHEMA = {"name": str, "priority": int}


def validate(raw):
    data = json.loads(raw)
    for key, typ in SCHEMA.items():
        if not isinstance(data.get(key), typ):
            raise ValueError(f"bad or missing field: {key}")
    if not 1 <= data["priority"] <= 5:
        raise ValueError("priority out of range")
    return data


if __name__ == "__main__":
    print(validate('{"name": "fix login", "priority": 2}'))
    try:
        validate('{"name": "fix login", "priority": 9}')  # right shape, wrong value
    except ValueError as e:
        print("rejected:", e)
