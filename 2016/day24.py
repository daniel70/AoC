# the maze is 185x41 and has 8 points
from collections import defaultdict

maze = []
mazed = {}
pois = {}
with open("input24.txt") as f:
    for line_nr, line in enumerate(f):
        line = line.strip()
        maze_line = []
        for char_nr, c in enumerate(line):
            if c == "#":
                maze_line.append(True)
                mazed[(char_nr, line_nr)] = True
            else:
                maze_line.append(False)
                mazed[(char_nr, line_nr)] = False
            if c.isdigit():
                pois[(char_nr, line_nr)] = c

        maze.append(maze_line)


def get_neighbours(x: int, y:int) -> list:
    return [(dx, dy) for dx, dy in [
        (x, y - 1), # U
        (x + 1, y), # R
        (x, y + 1), # D
        (x - 1, y), # L
    ] if not mazed[(dx, dy)]]


distances = defaultdict(list)
points = [(27, 29)]
found = False
step = 0
steps = set()
seen = set(points[0])
while not found:
    step += 1
    new_points = []
    for point in points:
        neighbours = get_neighbours(*point)
        for neighbour in neighbours:
            if neighbour not in seen:
                seen.add(neighbour)
                if neighbour in pois:
                    found = True
                    distances[(27, 29)].append((pois[neighbour], step))
                new_points.append(neighbour)
    points = new_points

