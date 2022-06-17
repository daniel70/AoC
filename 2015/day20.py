import math

goal = 33_100_000
ten = goal // 10
eleven = goal // 11


def divisors(n: int) -> set[int]:
    ds = set([1, n])
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            ds.add(i)
            ds.add(n // i)
    return ds


i = 0
found = False
while True:
    i += 1
    nrs = divisors(i)
    total = sum(nrs)
    if not found and total >= ten:
        print("Answer 1", i)
        found = True
    if len(nrs) <= 50 and total >= eleven:
        print("Answer 2", i)
        break

# 928440 is too high
