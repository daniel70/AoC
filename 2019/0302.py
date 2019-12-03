"""
Advent of Code 2019, day 3, puzzle 2
plane is a dictionary
the key is an x,y-coordinate, like (23, 45)
the value is another dictionary with, at most, 2 keys:
- 0: the number of steps it took wire 0 to get here
- 1: the number of steps it took wire 1 to get here
we check if the value already exists at the coordinate because
we don't want to overwrite it and the first visit counts.
"""
import collections as cl

# lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]  # steps 610
# lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]  # steps 410
# lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"]  # steps 30

lines = []
with open("input03.txt") as f:
    for line in f:
        lines.append(line)


def plot_path(path, nr):
    x, y, step_count = 0, 0, 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        if direction == "U":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x, y + i)]
                if nr not in coord.keys():
                    coord[nr] = step_count
            y = y + steps
        if direction == "D":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x, y - i)]
                if nr not in coord.keys():
                    coord[nr] = step_count
            y = y - steps
        if direction == "R":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x + i, y)]
                if nr not in coord.keys():
                    coord[nr] = step_count
            x = x + steps
        if direction == "L":
            for i in range(1, steps + 1):
                step_count += 1
                coord = plane[(x - i, y)]
                if nr not in coord.keys():
                    coord[nr] = step_count
            x = x - steps


paths = [line.split(",") for line in lines]
plane = cl.defaultdict(dict)
for nr, path in enumerate(paths):
    plot_path(path, nr)

print(
    min(
        [
            val[0] + val[1]
            for val in plane.values()
            if all(wire in val for wire in (0, 1))
        ]
    )
)
