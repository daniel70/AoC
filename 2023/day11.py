from itertools import combinations

instructions: list[tuple[int, int]] = []
with open("input11.txt") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == "#":
                instructions.append((x, y))

empty_x: set[int] = set(range(x)) - {x for x, _ in instructions}
empty_y: set[int] = set(range(y)) - {y for _, y in instructions}


def distance(points, factor: int):
    total = 0
    for p1, p2 in points:
        x1, y1 = p1
        x2, y2 = p2
        total += abs(x1 - x2) + abs(y1 - y2)
        total += len(set(range(min(x1, x2), max(x1, x2))) & empty_x) * (factor - 1)
        total += len(set(range(min(y1, y2), max(y1, y2))) & empty_y) * (factor - 1)
    return total


print("answer 1:", distance(combinations(instructions, 2), 2))
print("answer 2:", distance(combinations(instructions, 2), 1_000_000))
