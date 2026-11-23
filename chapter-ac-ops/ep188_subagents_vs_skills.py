"""EP188 · Subagents vs skills: a skill shares context, a subagent works in its own."""
main_context = ["user task"]

def use_skill(ctx, text):
    ctx.append(text)  # skill text lands in the same context
    return ctx

def run_subagent(task):
    own = [task, "lots of intermediate noise"]
    return "summary: " + task, own  # only the summary returns

use_skill(main_context, "skill: release steps")
summary, sub_ctx = run_subagent("scan logs")
main_context.append(summary)

assert "skill: release steps" in main_context
assert "lots of intermediate noise" not in main_context
assert len(sub_ctx) == 2
print("subagents vs skills ok:", main_context)
