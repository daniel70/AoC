from collections import defaultdict
from itertools import permutations, count

antennas = defaultdict(list)
answer1 = set()
answer2 = set()

for i, line in enumerate(open('input08.txt').readlines()):
    for j, char in enumerate(line.strip()):
        if char != '.':
            antennas[char].append((j, i))
width, height = j, i

for value in antennas.values():
    for a1, a2 in permutations(value, 2):
        x1, y1 = a1
        x2, y2 = a2
        dx, dy = x2 - x1, y2 - y1
        for m in count():
            if 0 <= x2 + (dx * m) <= width and 0 <= y2 + (dy * m) <= height:
                if m == 1:
                    answer1.add((x2 + (dx * m), y2 + (dy * m)))
                answer2.add((x2 + (dx * m), y2 + (dy * m)))
            else:
                break

print("answer 1:", len(answer1))
print("answer 2:", len(answer2))
