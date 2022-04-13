from collections import namedtuple
from string import ascii_uppercase

instructions = []
with open("input19.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        instructions.append(line)

Point = namedtuple("Point", "x y")
direction = "S"
pos = Point(instructions[0].index('|'), 0)
char = "|"
found = []
steps = 0

while True:
    steps += 1
    if direction == "N":
        pos = Point(x=pos.x, y=pos.y - 1)
    if direction == "S":
        pos = Point(x=pos.x, y=pos.y + 1)
    if direction == "E":
        pos = Point(x=pos.x - 1, y=pos.y)
    if direction == "W":
        pos = Point(x=pos.x + 1, y=pos.y)

    char = instructions[pos.y][pos.x]

    if char == "+":
        if direction in ["N", "S"]:
            if pos.x > 0 and instructions[pos.y][pos.x - 1] != ' ':
                direction = "E"
            else:
                direction = "W"
        else:
            if pos.y > 0 and instructions[pos.y - 1][pos.x] != ' ':
                direction = "N"
            else:
                direction = "S"
    elif char == ' ':
        break
    elif char in ascii_uppercase:
        found.append(char)


print("answer 1:", "".join(found))
print("answer 2:", steps)
