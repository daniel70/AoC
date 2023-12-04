import re
from collections import defaultdict

instructions = []
with open("input04.txt") as file:
    for line in file:
        line = line.strip()
        _, line = line.split(": ")
        instructions.append(line.strip())


total = 0
copies = defaultdict(int)
for nr, instruction in enumerate(instructions):
    nr += 1
    left, right = instruction.split(" | ")
    mine = {int(nr) for nr in re.findall(r"\d+", left)}
    winning = {int(nr) for nr in re.findall(r"\d+", right)}
    winners = len(mine & winning)
    if winners:
        total += 2 ** (winners - 1)
    for c in range(1, winners + 1):
        copies[nr + c] += copies[nr] + 1

print("answer 1:", total)
print("answer 2:", sum(copies.values()) + len(instructions))
