import math
import re
from collections import defaultdict

cubes = re.compile(r"(\d+) (\w+)")
instructions = []
with open("input02.txt") as file:
    for line in file:
        line = line.strip()
        match = cubes.findall(line)
        instructions.append(match)

answer1 = answer2 = 0
for nr, game in enumerate(instructions):
    bag = defaultdict(int)
    for value, color in game:
        bag[color] = max(int(value), bag[color])
    answer1 += nr + 1 if bag['red'] <= 12 and bag['green'] <= 13 and bag['blue'] <= 14 else 0
    answer2 += math.prod(bag.values())

print("answer 1:", answer1)
print("answer 2:", answer2)
