"""
Advent of Code 2019, day 1, puzzle 1
"""
l = []
with open("input01.txt") as f:
    for line in f:
        l.append(int(line))

total = 0
for mass in l:
    fuel = mass // 3 - 2
    total = total + fuel

print(total)
