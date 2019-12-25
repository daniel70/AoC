"""
Advent of Code 2019, day 7, puzzle 1
"""
with open("input08.txt") as f:
    line = f.readline()
line = line[:-1]

# line = "123456789012"

WIDE = 25
TALL = 6
SIZE = WIDE * TALL
layers = [line[i:i + SIZE] for i in range(0, len(line), SIZE)]
image = []
for l in range(SIZE):
    for layer in layers:
        if layer[l] != '2':
            image.append(layer[l])
            break

print(''.join(image))