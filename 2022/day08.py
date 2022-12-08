seen = set()
instructions = []
with open('input08.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append([])
        for char in line:
            instructions[-1].append(int(char))


W = len(instructions[0])
H = len(instructions)
transposed = [[] for _ in range(H)]
for y, row in enumerate(instructions):
    for x, height in enumerate(row):
        transposed[x].append(height)


for y, row in enumerate(instructions):
    heighest = - 1
    for x, height in enumerate(row):
        if height > heighest:
            seen.add((x, y))
            heighest = height

    heighest = - 1
    for x, height in enumerate(row[::-1]):
        if height > heighest:
            seen.add((W - 1 - x, y))
            heighest = height


for col in range(W):
    heighest = - 1
    for y, row in enumerate(instructions):
        height = row[col]
        if height > heighest:
            seen.add((col, y))
            heighest = height

    heighest = - 1
    for y, row in enumerate(instructions[::-1]):
        height = row[col]
        if height > heighest:
            seen.add((col, H - 1 - y))
            heighest = height


def scenic_score(x, y):
    global W
    global H
    global instructions
    global transposed

    # edge detection
    if x in (0, W-1) or y in (0, H-1):
        return 0

    me = instructions[y][x]
    left = right = up = down = 0

    for tree in instructions[y][x-1::-1]:
        left += 1
        if tree >= me:
            break

    for tree in instructions[y][x+1:]:
        right += 1
        if tree >= me:
            break

    for tree in transposed[x][y-1::-1]:
        up += 1
        if tree >= me:
            break

    for tree in transposed[x][y + 1:]:
        down += 1
        if tree >= me:
            break

    return left * right * up * down


print("answer 1:", len(seen))
scores = {(x, y): scenic_score(x, y) for x in range(W) for y in range(H)}
print("answer 2:", max(scores.values()))
