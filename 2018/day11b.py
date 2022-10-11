from sys import maxsize
from datetime import datetime as dt

serial = 3613
columns, rows = 300, 300
cells = {}
memoize = {}


def get_cell(x, y):
    return 300 * (y - 1) + x


def get_grid_cells(x, y, size):
    # return only the extra cells
    top_left = get_cell(x, y)
    grid_cells = []
    for dx in range(0, size):
        grid_cells.append(top_left + dx + (columns * (size - 1)))

    for dy in range(0, size):
        grid_cells.append(top_left + dx + (dy * columns))

    return grid_cells


def power(x, y, serial):
    rack_id = x + 10
    return ((rack_id * y + serial) * rack_id) % 1000 // 100 - 5


for x in range(1, columns + 1):
    for y in range(1, rows + 1):
        cell = get_cell(x, y)
        cells[cell] = power(x, y, serial)


def highest_grid(max_size):
    previous_highest = 0
    sizes = {}
    for size in range(1, max_size + 1):

        total = -maxsize
        highest = None
        for x in range(1, columns - size):
            for y in range(1, rows - size):
                square = 0
                for cell in get_grid_cells(x, y, size):
                    square += cells[cell]

                if size > 1:
                    square += memoize[(x, y, size - 1)]
                memoize[(x, y, size)] = square

                if square > total:
                    total = square
                    highest = (x, y, total)

        sizes[size] = (highest)


    return sizes


tick = dt.now()
sizes = highest_grid(300)
tock = dt.now()
print((tock - tick).total_seconds())
