from itertools import zip_longest
from functools import cmp_to_key


def is_correct(left, right) -> int | None:
    for l, r in zip_longest(left, right):
        match l, r:
            case None, int():
                return 1

            case int(), None:
                return -1

            case None, list():
                return 1

            case list(), None:
                return -1

            case int(), int():
                if l < r:
                    return 1
                if l > r:
                    return -1

            case list(), list():
                result = is_correct(l, r)
                if result != 0:
                    return result

            case list(), int():
                result = is_correct(l, [r])
                if result != 0:
                    return result

            case int(), list():
                result = is_correct([l], r)
                if result != 0:
                    return result

    return 0


combinations = open("input13.txt").read().split("\n\n")
lefts = [eval(c.split("\n")[0]) for c in combinations]
rights = [eval(c.split("\n")[1]) for c in combinations]
results = list(map(is_correct, lefts, rights))

score = 0
for idx, result in enumerate(results):
    if result == 1:
        score += idx + 1
print("answer 1:", score)

all_packets = lefts + rights + [[[2]]] + [[[6]]]
sorted_packets = sorted(all_packets, key=cmp_to_key(is_correct), reverse=True)
print("answer 2:",  (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
