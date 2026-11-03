"""EP099 · Agent engineer interview questions: a tiny flashcard drill over the three themes."""
import random

CARDS = {
    "loop": ["Draw the agent loop.", "What state must persist between turns?"],
    "tradeoffs": ["Single agent or multi-agent here, and why?", "How do you trade cost against quality?"],
    "failures": ["How do you defend against prompt injection?", "How would you debug a wrong answer from a trace?"],
}

if __name__ == "__main__":
    random.seed(7)
    for theme, qs in CARDS.items():
        print(f"[{theme}] {random.choice(qs)}")
