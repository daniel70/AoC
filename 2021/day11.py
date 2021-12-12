import math

grid = []
with open('input11.txt') as f:
    for line in f:
        line = line.strip()
        grid.extend([int(c) for c in line])
del f, line
W = H = int(math.sqrt(len(grid)))
T = W * H


def get_neighbours(idx):
    if not 0 <= idx < T:
        return []
    n = [idx - W - 1, idx - W, idx - W + 1, idx - 1, idx + 1, idx + W - 1, idx + W, idx + W + 1]
    return [cell for cell in n if 0 <= cell < T and abs(cell % W - idx % W) <= 1 ]


step = 0
flashes = 0
while True:
    step += 1

    flashed = [False] * T
    # increment all values with 1
    for idx in range(T):
        grid[idx] += 1

    has_flashed = True
    while has_flashed:
        has_flashed = False
        for idx in range(T):
            if grid[idx] > 9:
                has_flashed = True
                flashed[idx] = True
                grid[idx] = 0
                for nidx in get_neighbours(idx):
                    grid[nidx] += 1

    # reset flashed octopuses
    for idx in range(T):
        if flashed[idx]:
            flashes += 1
            grid[idx] = 0

    if step == 100:
        print('answer 1:', flashes)

    if all([cell for cell in flashed]):
        break

print('answer 2:', step)