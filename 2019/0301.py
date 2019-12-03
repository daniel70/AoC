"""
Advent of Code 2019, day 3, puzzle 1
plane is a dictionary
the key is an x,y-coordinate, like (23, 45)
the value is a set of wire numbers, either (0) or (1) or (0, 1) if both wires crossed this coordinate
"""
import collections as cl

# lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]  # distance 159
# lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]  # distance 135
# lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"]  # distance 6

lines = []
with open("input03.txt") as f:
    for line in f:
        lines.append(line)


def plot_path(path, nr):
    x, y = 0, 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        if direction == "U":
            for i in range(1, steps + 1):
                plane[(x, y + i)].add(nr)
            y = y + steps
        if direction == "D":
            for i in range(1, steps + 1):
                plane[(x, y - i)].add(nr)
            y = y - steps
        if direction == "R":
            for i in range(1, steps + 1):
                plane[(x + i, y)].add(nr)
            x = x + steps
        if direction == "L":
            for i in range(1, steps + 1):
                plane[(x - i, y)].add(nr)
            x = x - steps


paths = [line.split(",") for line in lines]
plane = cl.defaultdict(set)
for nr, path in enumerate(paths):
    plot_path(path, nr)

print(
    min(
        [
            abs(coord[0]) + abs(coord[1])
            for coord, wire in plane.items()
            if len(wire) > 1
        ]
    )
)
