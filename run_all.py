"""Smoke-run every sample and fail if any exits non-zero."""
import glob
import subprocess
import sys

failed = 0
for path in sorted(glob.glob("ep*.py")):
    r = subprocess.run([sys.executable, path], capture_output=True, text=True)
    print(("ok   " if r.returncode == 0 else "FAIL ") + path)
    if r.returncode:
        failed += 1
        print(r.stderr)
sys.exit(failed)
