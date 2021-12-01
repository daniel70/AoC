from itertools import pairwise, tee

lines = []
with open('input01.txt') as f:
    for line in f:
        lines.append(int(line))

count = 0
for x, y in pairwise(lines):
    if x < y:
        count += 1

print('puzzle 1:', count)

def triplewise(iterable):
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

count = -1
prev = 0
for x, y, z in triplewise(lines):
    if sum([x, y, z]) > prev:
        count += 1
    prev = sum([x, y, z])

print('puzzle 2:', count)

