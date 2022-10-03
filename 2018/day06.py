from collections import defaultdict

MAX_DISTANCE = 10_000

coordinates = defaultdict(list)
points: list[tuple[int, ...]] = []
most_points = 0
region = 0

with open("input06.txt") as f:
    for line in f:
        points.append(tuple(int(s) for s in line.split(",")))

max_x = max(x for x, y in points)
max_y = max(y for x, y in points)


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def all_manhattan_distances(points, point):
    distances = []
    for p in points:
        distances.append(manhattan_distance(p, point))
    return distances


for r in range(0, max_x + 1):
    for c in range(0, max_y + 1):
        dist = all_manhattan_distances(points, (r, c))
        if sum(dist) < MAX_DISTANCE:
            region += 1
        if dist.count(min(dist)) > 1:  # check for a tie
            continue
        coordinates[points[dist.index(min(dist))]].append((r, c))


# only keep coordinates if the point does not appear anywhere on the border
for k, v in coordinates.items():
    is_infinite = False
    for x, y in v:
        if x in (0, max_x) or y in (0, max_y):
            is_infinite = True

    if is_infinite:
        continue
    most_points = max(most_points, len(v))

print("answer1:", most_points)
print("answer2:", region)
