directions = {
    'n': (0, 1),
    'ne': (1, 0.5),
    'se': (1, -0.5),
    's': (0, -1),
    'sw': (-1, -0.5),
    'nw': (-1, 0.5),
}


def distance(instructions: list[str]) -> tuple[int, int]:
    origin = [0, 0]
    furthest = 0
    for direction in instructions:
        dx, dy = directions[direction]
        origin[0] += dx
        origin[1] += dy
        x, y = origin
        furthest = max(furthest, abs(x) + max(int(abs(y)) - abs(x) // 2, 0))

    steps = abs(x) + max(int(abs(y)) - abs(x) // 2, 0)
    return steps, furthest


instructions = open("input11.txt").read().strip().split(",")
answer1, answer2 = distance(instructions=instructions)
print("answer 1:", answer1)
print("answer 2:", answer2)
