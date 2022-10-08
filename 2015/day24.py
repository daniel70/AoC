from itertools import combinations
from functools import reduce
from operator import mul
packages = {int(line) for line in open("input24.txt").readlines()}


def quantum_entanglement(packages, buckets):
    weight = sum(packages) // buckets
    for i in range(1, len(packages)):
        possible = list(filter(lambda s: sum(s) == weight, combinations(packages, i)))
        if possible:
            answer = sorted(possible, key=lambda k: reduce(mul, k))[0]
            return reduce(mul, answer)


print("answer 1:", quantum_entanglement(packages, 3))
print("answer 2:", quantum_entanglement(packages, 4))
