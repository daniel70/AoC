"""
Advent of Code 2019, day 1, puzzle 2
Same as before, but now using recursion
"""


def fuel(mass):
    mass = mass // 3 - 2
    if mass <= 0:
        return 0
    else:
        return mass + fuel(mass)


total: int = 0
with open("input01.txt") as f:
    for line in f:
        total += fuel(int(line))

print(total)
