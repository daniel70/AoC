from itertools import pairwise

instructions = []
with open("input09.txt") as file:
    for line in file:
        line = line.strip()
        instructions.append([int(char) for char in line.split()])

answer1 = answer2 = 0
for instruction in instructions:
    history = [
        instruction,
    ]
    while not all(c == 0 for c in history[-1]):
        history.append([right - left for left, right in pairwise(history[-1])])

    for last, prev in pairwise(reversed(history)):
        pre = -last[0] + prev[0]
        post = last[-1] + prev[-1]
        prev.insert(0, pre)
        prev.append(post)

    answer1 += history[0][-1]
    answer2 += history[0][0]

print(answer1)
print(answer2)
