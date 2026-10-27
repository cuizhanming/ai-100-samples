"""EP043 · Idempotency and dry-run. An idempotency key makes a retried charge safe."""
charged = {}


def charge(key, amount, dry_run=False):
    if dry_run:
        return f"would charge {amount}"
    if key in charged:
        return f"duplicate ignored ({charged[key]} already charged)"
    charged[key] = amount
    return f"charged {amount}"


if __name__ == "__main__":
    print(charge("order-1", 50, dry_run=True))
    print(charge("order-1", 50))
    print(charge("order-1", 50))
