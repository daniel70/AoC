import re
from collections import defaultdict
from copy import deepcopy
from itertools import permutations

recompile = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.")
instructions = []
with open('input13.txt') as f:
    for line in f:
        m = recompile.match(line)
        if m:
            instructions.append(m.groups())
        else:
            print(f"no match for {line}")

party1 = defaultdict(dict)
for name, sign, val, neighbor in instructions:
    party1[name][neighbor] = ([1, -1][["gain", "lose"].index(sign)] * int(val))

friends = list(party1.keys())
party2 = deepcopy(party1)

for friend in friends:
    party2[friend]["Daniel"] = 0
    party2["Daniel"][friend] = 0


def calculate(seating):
    happiness = 0
    for l, r in zip(seating, seating[1:]):
        happiness += party[l][r]
        happiness += party[r][l]

    happiness += party[seating[0]][seating[-1]]
    happiness += party[seating[-1]][seating[0]]
    return happiness


seatings1 = permutations(party1.keys(), len(party1.keys()))
seatings2 = permutations(party2.keys(), len(party2.keys()))
party = party1
print('answer1: ', max(map(calculate, seatings1)))
party = party2
print('answer2: ', max(map(calculate, seatings2)))
