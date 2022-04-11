from itertools import combinations
total = total2 = 0
C = []
with open('input17.txt') as f:
    for line in f:
        C.append(int(line.strip()))

found = False  # used for second part
for r in range(1, len(C) + 1):
    for c in combinations(C, r):
        if sum(c) == 150:
            if not found:
                total2 += 1
            total += 1

    if total2 > 0:
        found = True

print('answer 1:', total)
print('answer 2:', total2)
