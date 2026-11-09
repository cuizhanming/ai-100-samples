"""EP122 · Sandboxing and egress: writes limited to the workspace, network to an allowlist."""
import posixpath

WORKSPACE = "/work/project"
ALLOWED_HOSTS = {"pypi.org"}


def can_write(path):
    p = posixpath.normpath(path)
    return p == WORKSPACE or p.startswith(WORKSPACE + "/")


def can_connect(host):
    return host in ALLOWED_HOSTS


assert can_write("/work/project/src/a.py")
assert not can_write("/work/project/../secrets/key")
assert not can_write("/home/me/.ssh/id_rsa")
assert can_connect("pypi.org") and not can_connect("evil.example")
print("sandbox rules ok")
