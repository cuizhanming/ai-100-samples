"""EP037 · Computer use. The screen loop: look, decide, act, repeat. The screen is simulated."""
SCREENS = {"home": ["Login"], "login": ["Submit"], "done": []}
NEXT = {"Login": "login", "Submit": "done"}


def decide(buttons):
    return buttons[0] if buttons else None


if __name__ == "__main__":
    screen, steps = "home", 0
    while (action := decide(SCREENS[screen])) and steps < 10:
        print(f"step {steps + 1}: on {screen!r}, click {action!r}")
        screen, steps = NEXT[action], steps + 1
    print("finished on", screen)
