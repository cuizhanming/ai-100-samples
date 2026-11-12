"""EP136 · Background tasks: start a slow command, keep working, poll output later."""
import subprocess
import sys

proc = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(0.3); print('build done')"],
                        stdout=subprocess.PIPE, text=True)
steps = []
while proc.poll() is None:
    steps.append("other work")  # the loop keeps going
out = proc.communicate()[0].strip()
assert out == "build done" and steps
print(f"{len(steps)} other steps ran; output: {out}")
print("background ok")
