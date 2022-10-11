from sys import maxsize

serial = 3613
grid_size = 300
grid = {}
memoize = {}


def get_power(x, y, serial):
    rack_id = x + 10
    return ((rack_id * y + serial) * rack_id) % 1000 // 100 - 5


def highest_grid(max_size):
    sizes = {}
    for size in range(1, max_size + 1):
        max_power = -maxsize
        cell_with_max_power = None
        for x in range(1, grid_size - size + 2):
            for y in range(1, grid_size - size + 2):
                power = 0
                # get the right and bottom values of the grid
                for dy in range(0, size - 1):
                    power += grid[(x + size - 1, y + dy)]
                for dx in range(0, size):
                    power += grid[(x + dx, y + size - 1)]

                # add to that the power of the inner grid
                if size > 1:
                    power += memoize[(x, y, size - 1)]
                # and store it for the next grid
                memoize[(x, y, size)] = power

                if power > max_power:
                    max_power = power
                    cell_with_max_power = (x, y, max_power)

        sizes[size] = cell_with_max_power
    return sizes


for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        grid[(x, y)] = get_power(x, y, serial)


sizes = highest_grid(300)
print("answer 1:", ",".join([str(x) for x in sizes[3][:2]]))
nr, cell = max(sizes.items(), key=lambda k: k[1][2])
answer2 = list(cell[:2])
answer2.append(nr)
print("answer 2:", ",".join([str(x) for x in answer2]))
