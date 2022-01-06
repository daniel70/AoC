import itertools as it


def change_direction(direction, turn):
    directions = ["N", "E", "S", "W"]
    if turn == "R":
        idx = directions.index(direction) + 1
    else:
        idx = directions.index(direction) - 1
    return directions[idx % 4]


def distance(steps):
    axes = it.cycle([0, 1])
    position = [0, 0]
    direction = "N"
    visited = [position.copy(), ]
    twice = None
    for step in steps:
        turn, length = step[0], int(step[1:])
        direction = change_direction(direction, turn)
        ax = next(axes)
        if direction in ["N", "E"]:
            for i in range(1, length + 1):
                position[ax] += 1
                if position in visited and not twice:
                    twice = position.copy()
                visited.append(position.copy())
        else:
            for i in range(length, 0, -1):
                position[ax] -= 1
                if position in visited and not twice:
                    twice = position.copy()
                visited.append(position.copy())

    return abs(position[0]) + abs(position[1]), abs(twice[0]) + abs(twice[1])


blocks, first = distance(open("input01.txt").readline().strip().split(", "))
print("answer 1:", blocks)
print("answer 2:", first)
