import math
from collections import Counter, defaultdict

transforms = defaultdict(list)
counter = Counter()


def most_least_difference(counter):
    total = Counter()
    for key, val in counter.items():
        for c in key:
            total[c] += val

    # characters are counted twice, uneven happens for first and last character
    for key, val in total.items():
        total[key] = math.ceil(val / 2)

    most_common = total.most_common()
    return most_common[0][1] - most_common[-1][1]


with open('input14.txt') as f:
    template = f.readline().strip()
    f.readline()
    for line in f:
        line = line.strip()
        l, r = line.split(" -> ")
        transforms[l[0] + r].append(l)
        transforms[r + l[1]].append(l)

# initialize counter
for pos in range(len(template) - 1):
    counter[template[pos:pos+2]] += 1

for i in range(40):
    if i == 10:
        print('answer 1:', most_least_difference(counter))

    temp = Counter()
    for key, val in transforms.items():
        for item in val:
            temp[key] += counter[item]
    counter = temp.copy()

print('answer 2:', most_least_difference(counter))
