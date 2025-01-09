from functools import cache

towels, _, *designs = open("input19.txt").read().splitlines()
towels = towels.split(", ")

@cache
def solve(pattern: str):
    return pattern == "" or sum(solve(pattern.removeprefix(towel)) for towel in towels if pattern.startswith(towel))

print("answer 1:", sum(map(bool, map(solve, designs))))
print("answer 2:", sum(map(int, map(solve, designs))))
