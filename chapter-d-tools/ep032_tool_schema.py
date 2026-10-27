"""EP032 · Tool schema design. A tight schema rejects bad calls before they run."""
SCHEMA = {
    "name": "set_unit",
    "properties": {"unit": {"enum": ["celsius", "fahrenheit"]}, "precision": {"type": int, "min": 0, "max": 3}},
    "required": ["unit"],
}


def validate(args):
    errors = [f"missing {k}" for k in SCHEMA["required"] if k not in args]
    p = SCHEMA["properties"]
    if "unit" in args and args["unit"] not in p["unit"]["enum"]:
        errors.append("unit must be one of " + ", ".join(p["unit"]["enum"]))
    if "precision" in args and not (isinstance(args["precision"], int) and 0 <= args["precision"] <= 3):
        errors.append("precision must be an int 0-3")
    return errors


if __name__ == "__main__":
    print(validate({"unit": "kelvin", "precision": 9}))
    print(validate({"unit": "celsius", "precision": 1}))
