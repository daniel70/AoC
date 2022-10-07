# we expect that the message will appear at the point where the height is the smallest
import re
from itertools import count
nrs = re.compile(r"(-?\d+)")
instructions = []
with open("input10.txt") as f:
    for line in f:
        line = line.strip()
        x, y, dx, dy = [int(x) for x in nrs.findall(line)]
        instructions.append((x, y, dx, dy))


def print_message(instructions) -> int:
    height = max(i[1] for i in instructions) - min(i[1] for i in instructions)
    for seconds in count():
        instructions = [(x + dx, y + dy, dx, dy) for x, y, dx, dy in instructions]
        new_height = max(i[1] for i in instructions) - min(i[1] for i in instructions)
        if new_height > height:
            break

        height = new_height

    message = [(x - dx, y - dy) for x, y, dx, dy in instructions]  # go back 1 second
    for y in range(min(y for x, y in message), max(y for x, y in message) + 1):
        for x in range(min(x for x, y in message), max(x for x, y in message) + 1):
            print("#", end="") if (x, y) in message else print(" ", end="")
        print()
    return seconds


print("answer 1:")
seconds = print_message(instructions)
print("answer 2:", seconds)