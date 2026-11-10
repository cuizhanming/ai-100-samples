"""EP126 · Why swarms drown in bureaucracy: pairwise channels grow as n(n-1)/2."""


def channels(n):
    return n * (n - 1) // 2


def useful_fraction(n, work_per_agent=10.0, cost_per_channel=0.5):
    work = n * work_per_agent
    overhead = channels(n) * cost_per_channel
    return work / (work + overhead)


assert channels(2) == 1 and channels(10) == 45
fr = [useful_fraction(n) for n in (2, 5, 10, 20)]
assert fr == sorted(fr, reverse=True)
for n, f in zip((2, 5, 10, 20), fr):
    print(f"{n:>2} agents: {channels(n):>3} channels, useful share {f:.0%}")
print("swarm overhead ok")
