"""
Advent of Code 2019, day 1, puzzle 2
"""
l = []
with open("input01.txt") as f:
    for line in f:
        l.append(int(line))

total = 0
for mass in l:
    while mass > 0:
        mass = mass // 3 - 2
        total = total + max(0, mass)

print(total)
