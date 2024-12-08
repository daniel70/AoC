from collections import defaultdict
from itertools import permutations

antennas = defaultdict(list)
antinodes = set()

for i, line in enumerate(open('input08.txt').readlines()):
    for j, char in enumerate(line.strip()):
        if char != '.':
            antennas[char].append((j, i))
width, height = j, i

for value in antennas.values():
    for a1, a2 in permutations(value, 2):
        x1, y1 = a1
        x2, y2 = a2
        antinodes.add((x2 + x2 - x1, y2 + y2 - y1))

print(antinodes)
print(len(antinodes))
print(len([(x, y) for x, y in antinodes if 0 <= x <= j and 0 <= y <= i]))