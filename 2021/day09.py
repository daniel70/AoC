from math import prod

points = []
W = H = 0
with open("input09.txt") as f:
    for line in f:
        if line:
            H += 1
            line = line.strip()
            W = len(line)
            points.extend([int(c) for c in line])


def neighbours(i):
    if not 0 <= i < W*H:
        return []
    adjacent = [i - 1, i + 1, i - W, i + W]
    return [n for n in adjacent if 0 <= n < W * H and abs(i % W - n % W) <= 1]


total = 0
for i in range(W*H):
    if all([points[n] > points[i] for n in neighbours(i)]):
        total += points[i] + 1

print('answer 1:', total)

# create basin map
basin = [False] * W * H
# mark all nines True
for idx, val in enumerate(points):
    if val == 9:
        basin[idx] = True

basins = []
while False in basin:
    # put the first False in a new basin and mark it True
    b = [basin.index(False)]
    basin[basin.index(False)] = True
    found = True
    while found:
        found = False
        for idx in b[:]:
            for n in neighbours(idx):
                if not basin[n]:
                    found = True
                    b.append(n)
                    basin[n] = True

    basins.append(b)


print('answer 2:', prod(sorted([len(b) for b in basins], reverse=True)[0:3]))
