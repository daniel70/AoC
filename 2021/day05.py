from collections import namedtuple, Counter
from itertools import repeat

lines = []
Line = namedtuple("Line", "x1 y1 x2 y2")
Point = namedtuple("Point", "x y")
with open('input05.txt') as f:
    for line in f:
        line = line.strip()
        lines.append(Line(*(map(int, line.replace("->", ",").split(",")))))


def get_points(line, diags=False):
    # only horizontal and vertical lines
    if not (line.x1 == line.x2 or line.y1 == line.y2) and not diags:
        return []

    if line.x1 < line.x2:
        range_x = range(line.x1, line.x2 + 1)
    elif line.x1 > line.x2:
        range_x = range(line.x1, line.x2 - 1, -1)
    else:
        range_x = repeat(line.x1)

    if line.y1 < line.y2:
        range_y = range(line.y1, line.y2 + 1)
    elif line.y1 > line.y2:
        range_y = range(line.y1, line.y2 - 1, -1)
    else:
        range_y = repeat(line.y1)

    return zip(range_x, range_y)


points = Counter()
for line in lines:
    for point in get_points(line):
        points[point] += 1

total: int = len([p for p in points.values() if p >= 2])
print(f'answer 1: {total}')

points = Counter()
for line in lines:
    for point in get_points(line, True):
        points[point] += 1

total: int = len([p for p in points.values() if p >= 2])
print(f'answer 2: {total}')

