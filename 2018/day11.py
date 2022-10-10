serial = 3613
# serial = 42
columns, rows = 300, 300


def get_cell(x, y):
    return 300 * (y - 1) + x


def get_grid_cells(x, y, size):
    top_left = get_cell(x, y)
    grid_cells = []
    for dx in range(0, size):
        for dy in range(0, size):
            grid_cells.append(top_left + dx + (dy * columns))
    return grid_cells


def power(x, y, serial):
    rack_id = x + 10
    return ((rack_id * y + serial) * rack_id) % 1000 // 100 - 5


assert power(122, 79, 57) == -5
assert power(217, 196, 39) == 0
assert power(101, 153, 71) == 4

cells = {}
for x in range(1, columns + 1):
    for y in range(1, rows + 1):
        cell = get_cell(x, y)
        cells[cell] = power(x, y, serial)


def highest_grid(max_size):
    previous_highest = 0
    sizes = {}
    for size in range(1, max_size + 1):

        total = 0
        highest = None
        for x in range(1, columns - size):
            for y in range(1, rows - size):
                square = 0
                for cell in get_grid_cells(x, y, size):
                    square += cells[cell]

                if square > total:
                    total = square
                    highest = (x, y, total)

        sizes[size] = (highest)
        # if total < previous_highest:
        #     break
        # else:
        #     previous_highest = total

    return sizes


sizes = highest_grid(18)
