import math
from sys import maxsize
cave = []
with open("input15.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            cave.extend(list(map(int, line)))


def distance_from_origin(idx, cave, width, scale):
    original_width = width // scale
    col = idx % width
    row = idx // width
    dx = col // original_width
    dy = row // original_width
    hor = col % original_width
    ver = row % original_width
    i = cave[ver * original_width + hor] + dx + dy
    if i > 9:
        return i - 9
    return i


def get_neighbours(point, cave):
    if not (0 <= point < len(cave)):
        return []
    n = [point - W, point - 1, point + 1, point + W]
    return [p for p in n if 0 <= p < len(cave) and abs(point % W - p % W) <= 1]


def shortest_path():
    # keep improving until there is nothing to improve
    improved = True
    while improved:
        improved = False
        for idx, cost in enumerate(costs):
            neighbours = get_neighbours(idx, cave)
            least = min([costs[n] for n in neighbours])
            if least + cave[idx] < cost:
                improved = True
                costs[idx] = least + cave[idx]

    return costs[-1]


for answer, scale in enumerate([1, 5]):
    W = int(math.sqrt(len(cave)))
    W *= scale
    costs = [maxsize] * W * W
    costs[0] = 0

    mini_cave = cave.copy()
    cave = [0] * W * W
    for i in range(W * W):
        cave[i] = distance_from_origin(i, mini_cave, W, scale)

    print(f'answer {answer + 1}:', shortest_path())
