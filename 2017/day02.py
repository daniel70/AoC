import itertools


def hilo(row: list[int]) -> int:
    return max(row) - min(row)


def divisable(row: list[int]) -> int:
    found = False
    for l, r in itertools.combinations(row, 2):
        if l > r and l % r == 0:
            return l // r
        elif r > l and r % l == 0:
            return r // l


instructions = open("input02.txt").readlines()
checksum1 = 0
checksum2 = 0
for instruction in instructions:
    row = [int(nr) for nr in instruction.strip().split()]
    checksum1 += hilo(row)
    checksum2 += divisable(row)

print("answer 1:", checksum1)
print("answer 2:", checksum2)
