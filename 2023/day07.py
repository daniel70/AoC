from collections import Counter
from functools import cmp_to_key


def cmp_poker(hand1, hand2):
    order = "23456789TJQKA"
    h1 = sorted(Counter(hand1).values(), reverse=True)
    h2 = sorted(Counter(hand2).values(), reverse=True)
    h1 += [order.index(card) for card in hand1]
    h2 += [order.index(card) for card in hand2]
    
    for x, y in zip(h1, h2):
        if x == y:
            continue
        return [-1, 1][x > y]
    return 0


def cmp_joker(hand1, hand2):
    order = "J23456789TQKA"
    c1 = Counter(hand1)
    c2 = Counter(hand2)
    j1 = c1.pop("J", 0)
    j2 = c2.pop("J", 0)
    h1 = sorted(c1.values(), reverse=True)
    h2 = sorted(c2.values(), reverse=True)
    h1 += [order.index(card) for card in hand1]
    h2 += [order.index(card) for card in hand2]
    if not h1[0] + j1 == h2[0] + j2:
        return [-1, 1][h1[0] + j1 > h2[0] + j2]
    
    for x, y in zip(h1[1:], h2[1:]):
        if x == y:
            continue
        return [-1, 1][x > y]
    return 0

cmp_poker_py3 = cmp_to_key(cmp_poker)
cmp_joker_py3 = cmp_to_key(cmp_joker)
import re

instructions = []
with open("input07.txt") as file:
    for line in file:
        line = line.strip()
        instructions.append(line.split())


instructions.sort(key=lambda t: cmp_poker_py3(t[0]))
print("answer 1:", sum([(nr + 1) * int(entry[1]) for nr, entry in enumerate(instructions)]))
instructions.sort(key=lambda t: cmp_joker_py3(t[0]))
print("answer 2:", sum([(nr + 1) * int(entry[1]) for nr, entry in enumerate(instructions)]))
