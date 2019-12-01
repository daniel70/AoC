from collections import defaultdict

import numpy as np
import re

r = re.compile('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
lines = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]
max_width = 0
max_height = 0
claims = []
claim_ids = set()
with open('input03.txt') as f:
    # for line in lines:
    for line in f:
        m = r.match(line)
        id, left, top, width, height = [int(x) for x in m.groups()]
        claims.append((id, left, top, width, height))
        claim_ids.add(id)
        max_width = max(max_width, left + width)
        max_height = max(max_height, top + height)

print(f'{max_width=}')
print(f'{max_height=}')
fabric = defaultdict(list)
for id, left, top, width, height in claims:
    for x in range(left, left + width):
        for y in range(top, top + height):
            cell = y * max_width + x
            if fabric[cell]:
                fabric[cell].append(id)
                claim_ids.difference_update(fabric[cell])
            fabric[cell].append(id)
print(fabric)
print(f'{claim_ids}')
