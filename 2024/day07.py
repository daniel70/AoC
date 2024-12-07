import itertools
import operator

def concat(a, b):
    return int(f"{a}{b}")


answer1 = set()
answer2 = set()
equations = dict()
ops = [operator.add, operator.mul, concat]

for line in open('input07.txt').readlines():
    left, right = line.split(':')
    equations[int(left)] = [int(x) for x in right.split()]

for k, v in equations.items():
    for attempt in itertools.product(ops, repeat=len(v)-1):
        temp = v[0]
        for op, val in zip(attempt, v[1:]):
            temp = op(temp, val)
        if temp == k:
            if concat not in attempt:
                answer1.add(k)
            answer2.add(k)

print(sum(answer1))
print(sum(answer2))
