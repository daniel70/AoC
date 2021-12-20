import re
from itertools import count

with open("input17.txt") as f:
    line = f.readline().strip()
# x1, x2, y1, y2 = map(int, re.findall(r"[-]?\d+", line))
x1, x2, y1, y2 = 20, 30, -10, -5

hor_staying = []
t = 0
for i in count():
    t += i
    if x1 <= t <= x2:
        hor_staying.append(i)
    if t > x2:
        break

hor = []
for i in range(1, x2):

