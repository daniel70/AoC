from enum import Enum


class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3


class Turn(Enum):
    LEFT = 0,
    RIGHT = 1,


def change_direction(direction, turn):
    match direction:
        case Direction.NORTH:
            return Direction.EAST if turn == Turn.RIGHT else Direction.WEST
        case Direction.EAST:
            return Direction.SOUTH if turn == Turn.RIGHT else Direction.NORTH
        case Direction.SOUTH:
            return Direction.WEST if turn == Turn.RIGHT else Direction.EAST
        case Direction.WEST:
            return Direction.NORTH if turn == Turn.RIGHT else Direction.SOUTH


def forward(node, direction):
    x, y = node
    match direction:
        case Direction.NORTH:
            y += 1
        case Direction.EAST:
            x += 1
        case Direction.SOUTH:
            y -= 1
        case Direction.WEST:
            x -= 1
    return x, y


lines = []
with open("input22.txt") as f:
    for line in f:
        lines.append(line.strip())

ox = len(lines[0]) // 2
oy = len(lines) // 2

infected = set()
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            infected.add((x - ox, oy - y))

node = (0, 0)
direction = Direction.NORTH
total_infected = 0
for step in range(10000):
    if node in infected:
        direction = change_direction(direction, Turn.RIGHT)
        infected.remove(node)
    else:
        direction = change_direction(direction, Turn.LEFT)
        infected.add(node)
        total_infected += 1

    node = forward(node, direction)

print("answer 1:", total_infected)

infected = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            infected[(x - ox, oy - y)] = "#"


node = (0, 0)
direction = Direction.NORTH
total_infected = 0
for step in range(10000000):
    if node not in infected:
        infected[node] = "W"
        direction = change_direction(direction, Turn.LEFT)
    elif infected[node] == "W":
        infected[node] = "#"
        total_infected += 1
    elif infected[node] == "#":
        infected[node] = "F"
        direction = change_direction(direction, Turn.RIGHT)
    elif infected[node] == "F":
        del infected[node]
        direction = change_direction(direction, Turn.RIGHT)
        direction = change_direction(direction, Turn.RIGHT)

    node = forward(node, direction)

print("answer 2:", total_infected)
