"""
Advent of Code 2019, day 3, puzzle 1 and 2
After looking at some other solutions I concluded that I was using the wrong data type.
Instead of a dict I should really use a list of tuples.
The lists (wire1 and wire2) are converted to a set and then the intersection (&)
gets all the intersection points.

The answer for puzzle one is the lowest distance from (0, 0), so the min() of x + y
The answer for puzzle two is the lowest number of steps it took, the minimal number of steps
is the first time the point occurs in the list of coordinates. Which is what index() does.
"""


def plot_path(path):
    coords = []
    x, y = 0, 0
    directions = [(s[0], int(s[1:])) for s in path]
    for direction, steps in directions:
        for i in range(1, steps + 1):
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1
            if direction == "R":
                x += 1
            if direction == "L":
                x -= 1

            coords.append((x, y))
    return coords


intersection_points = None
with open("input03.txt") as f:
    wire1 = plot_path(f.readline().split(","))
    wire2 = plot_path(f.readline().split(","))
    intersection_points = set(wire1) & set(wire2)

print("answer puzzle 1:", min([abs(x) + abs(y) for x, y in intersection_points]))
print("answer puzzle 2:", min([wire1.index(s) + wire2.index(s) for s in intersection_points]))
