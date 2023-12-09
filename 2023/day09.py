from itertools import pairwise

instructions = []
with open("input09.txt") as file:
    for line in file:
        line = line.strip()
        instructions.append([int(char) for char in line.split()])

total = 0
for instruction in instructions:
    history = [instruction, ]
    while not all(c == 0 for c in history[-1]):
        history.append([right - left for left, right in pairwise(history[-1])])

    for last, prev in pairwise(reversed(history)):
        new_value = last[-1] + prev[-1]
        prev.append(new_value)

    total += history[0][-1]

print(total)