"""EP082 · Triggers and webhooks: verify the signature, dedupe, then run."""
import hashlib
import hmac

SECRET = b"demo-secret"  # illustrative; load real secrets from the environment
seen = set()


def sign(body):
    return hmac.new(SECRET, body, hashlib.sha256).hexdigest()


def handle(body, signature, event_id):
    if not hmac.compare_digest(sign(body), signature):
        return "rejected: bad signature"
    if event_id in seen:
        return "ignored: duplicate"
    seen.add(event_id)
    return "run agent with untrusted payload: " + body.decode()


if __name__ == "__main__":
    b = b'{"event":"push"}'
    print(handle(b, sign(b), "e1"))
    print(handle(b, sign(b), "e1"))
    print(handle(b, "forged", "e2"))
