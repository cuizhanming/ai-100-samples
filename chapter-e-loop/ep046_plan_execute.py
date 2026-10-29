"""EP046 · Plan-and-execute. Plan first, run steps, replan when a step fails."""


def make_plan(goal):
    return ["fetch data", "clean data", "write report"]


def run_step(step, attempt):
    if step == "clean data" and attempt == 0:
        raise RuntimeError("source timed out")
    return f"{step}: ok"


def execute(goal):
    plan, log = make_plan(goal), []
    for step in plan:
        try:
            log.append(run_step(step, attempt=0))
        except RuntimeError as err:
            log.append(f"{step}: failed ({err}); replanning with a retry")
            log.append(run_step(step, attempt=1))
    return log


if __name__ == "__main__":
    for line in execute("weekly report"):
        print(line)
