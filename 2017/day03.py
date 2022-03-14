import itertools
instruction = 265149


def incr_memory(position: int) -> int:
    if position == 1:
        return 1
    # size is the width and height of the square
    # so for a square between 10 and 25 the size is 5
    for size in itertools.count(1, 2):
        if size ** 2 >= position:
            break

    # spiral_steps are the number of steps from the first value
    # in the square until the position. for 23 this would be 23 - 9 = 14
    spiral_steps = position - ((size - 2) ** 2)

    # the distance is calculated in two steps
    # 1. to the inside it will take size // 2 steps, so for size 5 this is 2
    # 2. around to the middle this is abs(spiral_steps % (size - 1) - inside)
    inside = size // 2
    around = abs(spiral_steps % (size - 1) - inside)
    return inside + around


def sum_memory(target: int) -> int:
    square = (0, 0)
    seen = {square: 1}
    steps = 0
    for direction in itertools.cycle('RULD'):
        # every time we go left or right we take an extra step
        if direction in ['L', 'R']:
            steps += 1
        for step in range(steps):
            idx = 'RULD'.index(direction)
            square = (square[0] + [1, 0, -1, 0][idx], square[1] + [0, 1, 0, -1][idx])
            x, y = square
            value = sum([
                seen.get((x+1, y), 0),
                seen.get((x+1, y+1), 0),
                seen.get((x, y+1), 0),
                seen.get((x-1, y+1), 0),
                seen.get((x-1, y), 0),
                seen.get((x-1, y-1), 0),
                seen.get((x, y-1), 0),
                seen.get((x+1, y-1), 0),
            ])
            seen[square] = value

            if value > target:
                return value


print("answer 1:", incr_memory(instruction))
print("answer 2:", sum_memory(instruction))
