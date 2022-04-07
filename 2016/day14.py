from functools import lru_cache
from hashlib import md5
import itertools as it
import re


@lru_cache(maxsize=50_000)
def get_hash(s: str, rounds: int = 0) -> str:
    for _ in range(rounds + 1):
        s = md5(s.encode("utf-8")).hexdigest()
    return s


def solve(rounds):
    three = re.compile(r"(.)\1{2}")
    keys = []
    salt = "cuanljph"
    found = False
    for step in it.count(0):
        if found:
            break
        index = salt + str(step)
        match = re.search(three, get_hash(index, rounds=rounds))
        if match:
            five = re.compile(match[1] + r"{5}")
            for sub_step in range(step + 1, step + 1_001):
                index = salt + str(sub_step)
                match = re.search(five, get_hash(index, rounds=rounds))
                if match:
                    keys.append(step)
                    if len(keys) == 64:
                        found = True
                    break

    return step - 1


print("answer 1:", solve(0))
print("answer 2:", solve(2016))
