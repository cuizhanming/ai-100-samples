"""EP035 · Shell execution. Gate commands with an allow-list and a timeout."""
import shlex
import subprocess

ALLOWED = {"echo", "ls", "pwd"}


def run_shell(command, timeout=5):
    argv = shlex.split(command)
    if not argv or argv[0] not in ALLOWED:
        return {"ok": False, "error": f"blocked: {argv[0] if argv else ''}"}
    r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
    return {"ok": r.returncode == 0, "output": r.stdout.strip()}


if __name__ == "__main__":
    print(run_shell("echo hello"))
    print(run_shell("rm -rf /tmp/x"))
