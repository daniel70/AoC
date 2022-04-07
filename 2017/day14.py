def knot_hash(key: str, rounds=1) -> str:
    numbers = list(range(256))
    lengths = []
    for c in key:
        lengths.append(ord(c))
    lengths.extend([int(x) for x in "17,31,73,47,23".split(",")])

    list(range(256))
    current_position = skip_size = 0
    for _ in range(rounds):
        for length in lengths:
            numbers = numbers[current_position:] + numbers[:current_position]
            numbers = list(reversed(numbers[:length])) + numbers[length:]
            numbers = numbers[-current_position:] + numbers[:-current_position]
            current_position += (length + skip_size)
            current_position %= len(numbers)
            skip_size += 1

    dense_hash = []
    for i in range(16):
        value = 0
        for j in range(16):
            value = value ^ numbers[i * 16 + j]
        dense_hash.append(value)

    return "".join([f"{x:02x}" for x in dense_hash])


instructions = open("input14.txt").read().strip()

disk = []
for row in range(128):
    hex_hash = knot_hash(f"{instructions}-{row}", rounds=64)
    row_hash = ""
    for h in hex_hash:
        row_hash += f"{int(h, 16):04b}"
    disk.append(row_hash)

squares = 0
for row in disk:
    squares += row.count("1")

print("answer 1:", squares)


def mark_regions(x, y):
    if disk[y][x] == '1':
        regions.add(y * 128 + x)

        if x > 0 and y * 128 + x - 1 not in regions:
            mark_regions(x - 1, y)
        if x < 127 and y * 128 + x + 1 not in regions:
            mark_regions(x + 1, y)
        if y > 0 and y * 128 + x - 128 not in regions:
            mark_regions(x, y - 1)
        if y < 127 and y * 128 + x + 128 not in regions:
            mark_regions(x, y + 1)


regions = set()
total = 0
for y, row in enumerate(disk):
    for x, bit in enumerate(row):
        if bit == '1' and y * 128 + x not in regions:
            mark_regions(x, y)
            total += 1

print("answer 2:", total)
