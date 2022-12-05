import string
from collections import deque, defaultdict
import re

instructions = []
with open('input05.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line)

moves = []
for instruction in instructions:
    instruction = instruction.strip()
    if instruction.startswith("move"):
        moves.append([int(x) for x in re.findall(r'\d+', instruction)])


def get_stacks(instructions):
    stacks = defaultdict(deque)
    for instruction in instructions:
        if instruction.startswith(" 1"):
            break

        for idx, pos in enumerate(range(1, len(instruction), 4)):
            if instruction[pos] in string.ascii_uppercase:
                stacks[idx].append(instruction[pos])

    for stack in stacks.values():
        stack.reverse()
    return stacks


def rearrange(stacks, moves, cratemover_9001=False):
    for n, source, target in moves:
        temp = deque()
        for _ in range(n):
            temp.append(stacks[source - 1].pop())

        if not cratemover_9001:
            temp.reverse()

        for _ in range(n):
            stacks[target - 1].append(temp.pop())

    answer = ""
    for stack in stacks.values():
        answer += stack.pop()
    return answer


print("answer 1:", rearrange(get_stacks(instructions), moves, False))
print("answer 2:", rearrange(get_stacks(instructions), moves, True))
