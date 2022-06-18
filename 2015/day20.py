import math


def divisors(n: int) -> set[int]:
    """
    fastest way to get all divisors is to go from 1 to the square root
    """
    numbers = {1, n}
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            numbers |= {n, n // i}  # add the number and its reciprocal
    return numbers


goal = int(open("input20.txt").readline())
i = 0
found = False
while True:
    i += 1
    nrs = divisors(i)
    ten = sum(nrs) * 10
    if not found and ten >= goal:
        print("Answer 1", i)
        found = True
    else:
        eleven = sum(n for n in nrs if i / n <= 50) * 11
        if eleven >= goal:
            print("Answer 2", i)
            break
