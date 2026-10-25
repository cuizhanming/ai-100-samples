"""EP012 · Agent vs workflow vs chatbot. Who decides the next step: the code or the model?"""


def fake_llm(prompt):
    return f"<llm:{prompt}>"


def chatbot(msg):
    return fake_llm(msg)  # one in, one out


def workflow(text):
    # the code fixes the steps; the model only fills them in
    summary = fake_llm("summarise " + text)
    return fake_llm("translate " + summary)


def agent(goal, choose_step):
    # the "model" (choose_step) picks the next step at run time
    state, steps = goal, []
    while (step := choose_step(state, steps)) != "done":
        steps.append(step)
    return steps


if __name__ == "__main__":
    print(chatbot("hi"))
    print(workflow("report"))
    print(agent("fix bug", lambda s, steps: ["read", "edit", "test", "done"][len(steps)]))
