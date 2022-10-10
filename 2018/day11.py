serial = 3613
columns, rows = 300, 300


def get_cell(x, y):
    return 300 * (y - 1) + x


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

total = 0
highest = None
for x in range(1, columns - 1):
    for y in range(1, rows - 1):
        square = sum([
            cells[get_cell(x, y)],
            cells[get_cell(x + 1, y)],
            cells[get_cell(x + 2, y)],
            cells[get_cell(x, y + 1)],
            cells[get_cell(x + 1, y + 1)],
            cells[get_cell(x + 2, y + 1)],
            cells[get_cell(x, y + 2)],
            cells[get_cell(x + 1, y + 2)],
            cells[get_cell(x + 2, y + 2)],
        ])
        if square > total:
            total = square
            highest = (x, y)
