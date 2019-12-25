"""
Advent of Code 2019, day 7, puzzle 1
"""
from collections import Counter

with open("input08.txt") as f:
    line = f.readline()
line = line[:-1]

# line = "123456789012"

WIDE = 25
TALL = 6
SIZE = WIDE * TALL
layers = [line[i:i + SIZE] for i in range(0, len(line), SIZE)]
print(f'{layers=}')
fewest_zeros = float('inf')
layer_with_fewest_zeros = None
for i, s in enumerate(layers):
    c = Counter(s)
    zeros = c.get('0', 0)
    # print(f'layer {i} has {zeros} zeros')
    if zeros < fewest_zeros:
        fewest_zeros = zeros
        layer_with_fewest_zeros = i

c = Counter(layers[layer_with_fewest_zeros])
answer = c.get('1', 0) * c.get('2', 0)
print(f'{answer=}')