import itertools
import operator

hits = set()
equations = dict()
for line in open('input07.txt').readlines():
    left, right = line.split(':')
    equations[int(left)] = [int(x) for x in right.split()]


def concat(a, b):
    return int(f"{a}{b}")

ops = [operator.add, operator.mul, concat]

for k, v in equations.items():
    found = False
    for attempt in itertools.product(ops, repeat=len(v)-1):
        temp = v[0]
        for op, val in zip(attempt, v[1:]):
            temp = op(temp, val)
        if temp == k:
            found = True
            hits.add(k)

print(sum(hits))
